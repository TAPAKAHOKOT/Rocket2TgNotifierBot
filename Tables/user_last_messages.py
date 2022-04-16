from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    DateTime,
    text
)
from sqlalchemy.orm import (
    relationship
)

from datetime import datetime

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel

class UserLastMessages(Base, BaseModel):
    __tablename__ = 'user_last_messages'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete="CASCADE"), nullable=True)

    rocket_message_id = Column(String(256), nullable=True)
    rocket_updated_at = Column(String(256), nullable=True)

    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    
    user = relationship(
        'User',
        lazy='joined'
    )


    def get_class(self):
        return UserLastMessages


user_last_messages_table = UserLastMessages.__table__