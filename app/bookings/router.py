from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)

@router.get('')
async def get_bookings():
    return await BookingDAO.find_one_or_none(room_id=1)



