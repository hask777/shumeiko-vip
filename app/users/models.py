from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, JSON, Date, Computed

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    hashed_password = Column(String)

    