from fastapi import APIRouter
from core.schemas import User_By_Product
from service.tgbot import BotRequestsRepository

router = APIRouter(prefix='/api/v1', tags=['Set_Methods'])

@router.post('/set_by_user_card')
async def set_by_user_card(user: User_By_Product):
    card_info = await BotRequestsRepository.post_request_user_product(user)
    return {"user_product": card_info}

@router.get('/get_request_user_product/{tg_id}')
async def get_request_user_product(tg_id: int):
    request_info = await BotRequestsRepository.get_request_user_product(tg_id=tg_id)
    return {"request_info": request_info}