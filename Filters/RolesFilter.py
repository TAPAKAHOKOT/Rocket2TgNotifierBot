from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types import Message

from Tables import Role


class RolesFilter(BoundFilter):
    async def check(self, message: Message):
        data = ctx_data.get()
        user_role: Role = data['role']

        role = user_role.role if user_role else None

        return {
            'is_root': role == 'root',
            'is_admin': role in ['root', 'admin']
        }