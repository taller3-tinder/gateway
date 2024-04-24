from typing import Annotated
from dotenv import load_dotenv
import os
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
import requests
from gateway.app.middleware.firebase import get_current_user
from tinderlibs.schemas.swipes import UserSwipe
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/swipes",
    tags=['Swipes'],
    dependencies=[Depends(get_current_user)]
)


load_dotenv()
SWIPES_URL = os.getenv("SWIPES_URL")


@router.post('/')
def add_user_swipe(swipe: UserSwipe,
                   current_user: Annotated[dict, Depends(get_current_user)]):
    """
    Adds a Swipe to the Tinder System.
    """
    swipe = jsonable_encoder(swipe)
    swipe['swiper'] = current_user["uid"]
    resp = requests.post(f"{SWIPES_URL}/swipes", json=swipe)
    return JSONResponse(content=resp.json(), status_code=resp.status_code)
