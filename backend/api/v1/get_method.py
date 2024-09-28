from fastapi import APIRouter
from core.database.requests import CardRepository, PromocodRepository, BotRequestsRepository

router = APIRouter(prefix='/api/v1', tags=['Get_Info'])

@router.get('/get_card')
async def get_card_info():
    card_info = await CardRepository.get_card_info()
    if card_info:
        return card_info
    else:
        return {'error': 'No such card'}

@router.get('/get_request_user_product/{tg_id}')
async def get_request_user_product(tg_id: int):
    request_info = await BotRequestsRepository.get_request_user_product(tg_id=tg_id)
    return {"request_info": request_info}

@router.get('/get_promocod')
async def get_promocod_info():
    promocod_info = await PromocodRepository.get_promocod_info()
    if promocod_info:
        return promocod_info
    else:
        return {'error': 'No such promocod'}

