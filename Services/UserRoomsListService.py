from sqlalchemy import (
    and_
)
from sqlalchemy.orm import Session
from Database import engine

from Tables import (
    User,
    UserSettings,
    UserRoomsLists,
    user_rooms_lists
)
from Services import (
    NotificationsService
)
from Callbacks import user_rooms_list_callback

class UserRoomListService:
    @staticmethod
    def get_list_callback(user: User, user_settings: UserSettings, list_type: str):
        with Session(engine, expire_on_commit=False) as session, session.begin():
            user_rooms_lists: UserRoomsLists = UserRoomsLists.find_by_user_id(session, user.id)

        subs = UserRoomListService.get_user_subscriptions(user_settings)
        user_list = UserRoomListService.get_user_list(user_rooms_lists, list_type)

        callback_buttons = []
        for sub in subs['update']:
            rid = sub['rid']
            name = sub['name']
            callback_button = {
                'type': list_type,
                'turned_on': False,
                'rid': rid,
                'name': name
            }

            if rid in user_list:
                callback_button['turned_on'] = True
            
            callback_buttons.append(callback_button)
        return user_rooms_list_callback.get_list_inline(callback_buttons)


    @staticmethod
    def get_user_subscriptions(user_settings: UserSettings) -> dict|None:
        response_data = NotificationsService.get_response_data(
            user_settings.rocket_domain,
            user_settings.rocket_user_id,
            user_settings.rocket_token
        )

        return NotificationsService.get_subscriptions(response_data)


    @staticmethod
    def get_user_list(user_rooms_lists: UserRoomsLists, list_type: str) -> dict|None:
        return [l.rocket_room_id for l in user_rooms_lists if l.list_type == list_type]

    
    @staticmethod
    def add_to_list(user: User, list_type: str, rid: str):
        with Session(engine) as session, session.begin():
            user_rooms_list: UserRoomsLists = UserRoomsLists(
                user_id = user.id,
                list_type = list_type,
                rocket_room_id = rid
            )

            session.add(user_rooms_list)


    @staticmethod
    def remove_from_list(list_type: str, rid: str):
        with Session(engine) as session, session.begin():
            session.query(UserRoomsLists).filter(
                    and_(UserRoomsLists.rocket_room_id==rid, UserRoomsLists.list_type==list_type)
                ).delete()