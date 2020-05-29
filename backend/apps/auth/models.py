from sqlalchemy import Boolean, Column, Integer, String

from apps.core.database import Base


class User(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True, index=True)
    is_admin = Column(Boolean, default=False, index=True)

