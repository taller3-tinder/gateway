from typing import Annotated
from fastapi import APIRouter, Depends
from ..middleware.firebase import get_current_user
from ..schemas.users import RegisterUser
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/users",
    tags=['Users'],
    dependencies=[Depends(get_current_user)]
    # En los metodos que se necesita el current user,
    # el resultado es cacheado y no se vuelve a llamar 
    # a este metodo.
)


def join_attributes(user_schema, current_user):
    user = jsonable_encoder(user_schema)
    user["uid"] = current_user["uid"]
    user["email"] = current_user["email"]
    return user


@router.get('/{user_id}')
def find_user(user_id: str,
              current_user: Annotated[dict, Depends(get_current_user)]):
    print(f'El current user es {current_user["uid"]}')
    print(f'El user a obtener es {user_id}')


@router.post('/register')
def register_user(user_register: RegisterUser,
                  current_user: Annotated[str, Depends(get_current_user)]):
    user = join_attributes(user_register, current_user)
    print(f'El current user a crear es {user}')


@router.put('/')
def update_user(user_update: RegisterUser,
                current_user: Annotated[str, Depends(get_current_user)]):
    user = join_attributes(user_update, current_user)
    print(f'El current user a actualizar es {user}')


@router.delete('/')
def delete_user(current_user: Annotated[str, Depends(get_current_user)]):
    print(f'El current user a eliminar es {current_user["uid"]}')
