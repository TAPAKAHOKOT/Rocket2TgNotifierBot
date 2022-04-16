from sqlalchemy.orm import Session

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

from datetime import datetime

from Database import engine
from Tables import User

class UserMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        chat_id = message.from_user['id']
        username = message.from_user['username']

        with Session(engine) as session, session.begin():
            user: User = User.find_by_chat_id(session, chat_id)

            if not user:
                user = User(
                    chat_id=chat_id,
                    username=username
                )
            user.last_activity_at = datetime.now()

            session.add(user)
            
            data['user'] = user
            data['user_relations'] = {
                'role': user.role
            }


        