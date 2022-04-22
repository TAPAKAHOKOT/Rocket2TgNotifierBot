import requests as r
import logging

from sqlalchemy.orm import Session

from Database import engine

from Tables import (
    User,
    UserSettings,
    UserLastMessages,
    user_last_messages_table
)

class NotificationsService:
    @staticmethod
    def update_notifications(user: User, user_settings: UserSettings, user_last_messages: list):
        messages = NotificationsService.load_messages(
            user_settings.rocket_domain,
            user_settings.rocket_user_id,
            user_settings.rocket_token
        )
        new_messages = NotificationsService.get_all_new_messages(messages, user_last_messages)
        
        NotificationsService.delete_old_messages_in_db(user)
        NotificationsService.load_new_messages_in_db(user, messages)

        return new_messages


    @staticmethod
    def delete_old_messages_in_db(user: User):
        with Session(engine) as session, session.begin():
            session.query(UserLastMessages).filter(UserLastMessages.user_id==user.id).delete()

    @staticmethod
    def load_new_messages_in_db(user: User, new_messages: dict):
        with Session(engine) as session, session.begin():
            for id, message in new_messages.items():
                user_last_message: UserLastMessages = UserLastMessages(
                    user_id=user.id,
                    rocket_message_id=id,
                    rocket_updated_at=message['updated_at']
                )
                session.add(user_last_message)


    @staticmethod
    def get_all_new_messages(messages: dict, user_last_messages: list) -> dict:
        if not messages:
            return {}
            
        messages_id = messages.keys()
        user_last_messages = {m.rocket_message_id: m.rocket_updated_at for m in user_last_messages}

        new_messages = {}
        for id in messages_id:
            if id not in user_last_messages.keys():
                new_messages[id] = messages[id]
                new_messages[id]['is_reply'] = False
            elif user_last_messages[id] != messages[id]['updated_at']:
                new_messages[id] = messages[id]
                new_messages[id]['is_reply'] = True
        
        return new_messages


    @staticmethod
    def get_response_data(domain: str, user_id: str, token: str):
        return {
            'domain': 'https://' + domain + '/api/v1/',
            'headers': {
                'X-Auth-Token': token,
                'X-User-Id': user_id
            }
        }
    
    @staticmethod
    def get_response(data: dict, api: str):
        try:
            return r.get(data['domain'] + api, headers=data['headers'])
        except (r.exceptions.MissingSchema, r.exceptions.ConnectionError) as e:
            logging.error(f'Error: {str(e)}, data: {data}')
    
    @staticmethod
    def load_messages(domain: str, user_id: str, token: str):
        response_data = NotificationsService.get_response_data(domain, user_id, token)
        subs_response = NotificationsService.get_response(response_data, 'subscriptions.get')

        if (not subs_response) or (subs_response.status_code != 200):
            return None
        
        subs = subs_response.json()
        unread_subs = [sub['rid'] for sub in subs['update'] if sub['alert']]

        rooms_response = NotificationsService.get_response(response_data, 'rooms.get')

        if (not rooms_response) or (rooms_response.status_code != 200):
            return None

        rooms = rooms_response.json()
        unread_messages = {}

        for room in rooms['update']:
            if 'lastMessage' not in room.keys():
                continue

            last_message = room['lastMessage']
            rid = last_message['rid']

            if rid in unread_subs:
                unread_messages[last_message['_id']] = {
                        'updated_at': room['_updatedAt'],
                        'data': {
                            'room_name': room['name'] if 'name' in room.keys() else ' => '.join(room['usernames']),
                            'text': last_message['msg'],
                            'author': {
                                'name': last_message['u']['name'],
                                'username': last_message['u']['username']
                            }
                        }
                    }
        
        if unread_messages:
            return unread_messages
        return None