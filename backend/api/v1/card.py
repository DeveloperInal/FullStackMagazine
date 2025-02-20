from fastapi import APIRouter
from core.schemas import Card_UC_Data
from service.card import CardRepository

router = APIRouter(prefix='/api/v1', tags=['Set_Methods'])
@router.get('/get_card')
async def get_card_info():
    card_info = await CardRepository.get_card_info()
    if card_info:
        return card_info
    else:
        return {'error': 'No such card'}

@router.post('/set_card')
async def set_card_info(data: Card_UC_Data):
    card_info = await CardRepository.set_card_info(data)
    return {"card_info": card_info}

