from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, JSON, Date, Computed

class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    services = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)
    