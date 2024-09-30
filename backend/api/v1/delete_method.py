from fastapi import APIRouter
from core.database.requests import PromocodRepository

router = APIRouter(prefix='/api/v1', tags=['Delete_Methods'])

@router.delete('/delete_promocod')
async def delete_promocod_info(promocode: str):
    promocod_info = await PromocodRepository.delete_promocode(promocode=promocode)
    if promocod_info:
        return {"deleted": promocod_info}
    else:
        return {"error": "No such promocod"}