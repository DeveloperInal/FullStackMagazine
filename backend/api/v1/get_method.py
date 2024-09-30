from fastapi import APIRouter
from core.database.requests import CardRepository, BotRequestsRepository, AdminRepository, PromocodRepository

router = APIRouter(prefix='/api/v1', tags=['Get_Methods'])

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

@router.get('/get_promocode_by_title')
async def get_promocode_by_title(promocode_title: str):
    promocod_info = await PromocodRepository.get_promocodes_by_title(title=promocode_title)
    if promocod_info:
        return promocod_info
    else:
        return {'error': 'No such promocod'}
@router.get('/get_user_by_promocode')
async def get_user_promocod_info():
    users_info = await AdminRepository.get_user_by_promocode()
    if users_info:
        return users_info
    else:
        return {'error': 'No such promocod'}

@router.get('/get_promocode')
async def get_promocod_info():
    promocod_info = await PromocodRepository.get_promocode_info()
    if promocod_info:
        return promocod_info
    else:
        return {'error': 'No such promocod'}

