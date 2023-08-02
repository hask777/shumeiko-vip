from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from typing import List


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)

@router.get('')
async def get_bookings() -> List[SBooking]:
    return await BookingDAO.find_all()



