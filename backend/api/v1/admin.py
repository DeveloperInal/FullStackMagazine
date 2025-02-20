from fastapi import APIRouter
from service.admin import AdminRepository

router = APIRouter(prefix='/api/v1', tags=['Get_Methods'])

@router.get('/get_user_by_promocode')
async def get_user_promocod_info():
    users_info = await AdminRepository.get_user_by_promocode()
    if users_info:
        return users_info
    else:
        return {'error': 'No such promocod'}