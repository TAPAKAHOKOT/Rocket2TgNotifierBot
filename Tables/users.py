from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    DateTime,
    text,
    or_
)
from sqlalchemy.orm import (
    relationship,
    Session
)

from datetime import datetime

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel
from Tables.user_settings import UserSettings
from Tables.roles import Role

class User(Base, BaseModel):
    __tablename__ = 'users'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    role_id = Column(ForeignKey('roles.id', ondelete="SET NULL"), nullable=True)

    chat_id = Column(Integer, nullable=False, unique=True)
    username = Column(String(256), nullable=True)

    last_activity_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    
    role = relationship(
        'Role',
        lazy='joined'
    )

    user_settings = relationship(
        'UserSettings',
        lazy='joined',
        uselist=False,
        backref='user_settings'
    )

    user_last_messages = relationship(
        'UserLastMessages',
        lazy='joined'
    )

    user_rooms_lists = relationship(
        'UserRoomsLists',
        lazy='joined'
    )


    def get_class(self):
        return User

    
    def find_by_chat_id(session: Session, chat_id: int) -> 'User':
        return session.query(User).where(
                User.chat_id == chat_id
            ).first()
    
    def get_all_users(session: Session) -> list:
        return session.query(User).all()


    def get_all_users_with_notifications(session: Session) -> list:
        return session.query(User).join(UserSettings).where(
            UserSettings.send_notifications == True
        ).all()
    

    def get_all_admins(session: Session) -> list:
        return session.query(User).join(Role).where(
            or_(Role.role == 'root', Role.role == 'admin')
        ).all()


users_table = User.__table__