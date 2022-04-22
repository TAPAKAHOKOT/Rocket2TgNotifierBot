from sqlalchemy.orm import Session

from asyncio import sleep as asleep
from aioschedule import (
    every as schedule_every, 
    run_pending as schedule_run_pending
)

from Database import engine
from Services.NotificationsService import NotificationsService
from Tables import (
    User,
    UserSettings
)
from Settings import settings

class ScheduleService:
    @staticmethod
    async def run_schedule():
        schedule_every(30).seconds.do(ScheduleService.update_users_notifications)

        while True:
            await schedule_run_pending()
            await asleep(30)

    @staticmethod
    async def update_users_notifications():
        with Session(engine, expire_on_commit=False) as session, session.begin():
            for user in User.get_all_users_with_notifications(session):
                await ScheduleService.send_user_new_messages(user, user.user_settings, user.user_last_messages)
    
    @staticmethod
    async def send_user_new_messages(user: User, user_settings: UserSettings, user_last_messages: list):
        new_messages = NotificationsService.update_notifications(user, user_settings, user_last_messages)
        for new_message in new_messages.values():
            data = new_message['data']

            message_text = '[ {room} ]'.format(
                    room=data['room_name']
                )

            if not new_message['is_reply']:
                message_text += '\n\n{text}\n\n© {author_name} [ {author_username} ]'.format(
                    text=data['text'],
                    author_name=data['author']['name'],
                    author_username=data['author']['username']
                )
                

            await settings.bot.send_message(
                user.chat_id,
                message_text
            )



