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


    def get_class(self):
        return User

    
    def find_by_chat_id(session: Session, chat_id: int) -> 'User':
        return session.query(User).where(
                User.chat_id == chat_id
            ).first()


users_table = User.__table__