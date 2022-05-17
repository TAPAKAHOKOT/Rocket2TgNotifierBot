from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    DateTime,
    text
)
from sqlalchemy.orm import (
    relationship,
    Session
)

from datetime import datetime

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel
from Tables.users import User

class UserRoomsLists(Base, BaseModel):
    __tablename__ = 'user_rooms_lists'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete="CASCADE"), nullable=True)

    list_type = Column(String(256), nullable=False)
    rocket_room_id = Column(String(256), nullable=False)

    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    
    user = relationship(
        'User',
        lazy='joined'
    )

    def find_by_user_id(session: Session, id) -> list:
        return session.query(UserRoomsLists).join(User).where(
            User.id == id
        ).all()


    def get_class(self):
        return UserRoomsLists


user_rooms_lists_table = UserRoomsLists.__table__