import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from ..middleware.firebase import get_current_user
from ..schemas.users import RegisterUser
from fastapi.encoders import jsonable_encoder
import requests


router = APIRouter(
    prefix="/users",
    tags=['Users'],
    dependencies=[Depends(get_current_user)]
    # En los metodos que se necesita el current user,
    # el resultado es cacheado y no se vuelve a llamar 
    # a este metodo.
)

load_dotenv()
USERS_URL = os.getenv("USERS_URL")


def join_attributes(user_schema, current_user):
    user = jsonable_encoder(user_schema)
    user["id"] = current_user["uid"]
    user["email"] = current_user["email"]
    return user


@router.get('/{user_id}')
def find_user(user_id: str,
              current_user: Annotated[dict, Depends(get_current_user)]):
    resp = requests.get(f"{USERS_URL}/users/{user_id}/{current_user['uid']}")
    return JSONResponse(content=resp.json(), status_code=resp.status_code)


@router.post('/')
def register_user(user_register: RegisterUser,
                  current_user: Annotated[str, Depends(get_current_user)]):
    user = join_attributes(user_register, current_user)
    resp = requests.post(f"{USERS_URL}/users", json=user)
    return JSONResponse(content=resp.json(), status_code=resp.status_code)


@router.put('/')
def update_user(user_update: RegisterUser,
                current_user: Annotated[str, Depends(get_current_user)]):
    user = join_attributes(user_update, current_user)
    resp = requests.put(f"{USERS_URL}/users", json=user)
    return JSONResponse(content=resp.json(), status_code=resp.status_code)


@router.delete('/')
def delete_user(current_user: Annotated[str, Depends(get_current_user)]):
    resp = requests.delete(f"{USERS_URL}/users/{current_user['uid']}")
    return JSONResponse(content=resp.json(), status_code=resp.status_code)
