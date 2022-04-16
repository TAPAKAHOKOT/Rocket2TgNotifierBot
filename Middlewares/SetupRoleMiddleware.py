from sqlalchemy.orm import Session

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

from os import getenv

from Database import engine
from Tables import (
    Role,
    User
)

class SetupRoleMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        admins = map(int, getenv("ADMINS").split(','))
        chat_id = message.from_user['id']

        if chat_id not in admins:
            return

        with Session(engine) as session, session.begin():
            user: User = User.find_by_chat_id(session, chat_id)
            role: Role = Role.find_by_role(session, 'root')

            if user and role:
                user.role_id = role.id
                session.add(user)


        