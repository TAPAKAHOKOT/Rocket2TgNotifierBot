from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types import Message

from Tables import Role


class IsAdminFilter(BoundFilter):
    async def check(self, message: Message) -> bool:
        user_role: Role = ctx_data.get()['role']

        role = user_role.role if user_role else None

        return role == 'root'