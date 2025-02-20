from fastapi import APIRouter
from core.schemas import Promocod_Data
from service.promocode import PromocodeRepository
router = APIRouter(prefix='/api/v1', tags=['Set_Methods'])


@router.get('/get_promocode')
async def get_promocod_info():
    promocod_info = await PromocodeRepository.get_promocode_info()
    if promocod_info:
        return promocod_info
    else:
        return {'error': 'No such promocod'}

@router.get('/get_promocode_by_title')
async def get_promocode_by_title(promocode_title: str):
    promocod_info = await PromocodeRepository.get_promocodes_by_title(title=promocode_title)
    if promocod_info:
        return promocod_info
    else:
        return {'error': 'No such promocod'}

@router.post('/set_promocod')
async def set_promocod_info(data: Promocod_Data):
    promocod_info = await PromocodeRepository.set_promocode_info(promocode=data)
    return {"promocod_info": promocod_info}

@router.delete('/delete_promocod')
async def delete_promocod_info(promocode: str):
    promocod_info = await PromocodeRepository.delete_promocode(promocode=promocode)
    if promocod_info:
        return {"deleted": promocod_info}
    else:
        return {"error": "No such promocod"}