from core.database.requests import CardRepository, PromocodRepository, BotRequestsRepository
from core.schemas import Promocod_Data, Card_UC_Data, User_By_Product
from fastapi import APIRouter

router = APIRouter(prefix='/api/v1', tags=['Set_Info'])

@router.post('/set_card')
async def set_card_info(data: Card_UC_Data):
    card_info = await CardRepository.set_card_info(data)
    return {"card_info": card_info}

@router.post('/set_by_user_card')
async def set_by_user_card(user: User_By_Product):
    card_info = await BotRequestsRepository.post_request_user_product(user)
    return {"user_product": card_info}

@router.post('/set_promocod')
async def set_promocod_info(data: Promocod_Data):
    promocod_info = await PromocodRepository.set_promocod_info(promocode=data)
    return {"promocod_info": promocod_info.promocod}