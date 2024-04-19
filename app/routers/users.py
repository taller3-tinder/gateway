from typing import Annotated
from fastapi import APIRouter, Depends
from ..middleware.firebase import get_current_user

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get('/{user_id}')
def find_user(user_id: str,
              current_user: Annotated[str, Depends(get_current_user)]):
    print(f'El current user es {current_user}')
    print(f'El user a obtener es {user_id}')
