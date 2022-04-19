from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Boolean,
    Integer,
    DateTime,
    text
)

from datetime import datetime

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel
from Configs import get_default_language

class UserSettings(Base, BaseModel):
    __tablename__ = 'user_settings'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete="CASCADE"), nullable=True)

    language = Column(String(256), nullable=True, default=get_default_language())
    send_notifications = Column(Boolean, default=False, nullable=False)
    rocket_domain = Column(String(256), nullable=True)
    rocket_token = Column(String(256), nullable=True)
    rocket_user_id = Column(String(256), nullable=True)

    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))


    def get_class(self):
        return UserSettings


user_settings_table = UserSettings.__table__