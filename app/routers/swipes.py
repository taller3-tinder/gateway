from dotenv import load_dotenv
import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from tinderlibs.schemas.swipes import SwipeBase
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/swipes",
    tags=['Swipes']
)


load_dotenv()
SWIPES_URL = os.getenv("SWIPES_URL")


@router.post('/')
def add_user_swipe(swipe: SwipeBase):
    """
    Adds a Swipe to the Tinder System.
    """
    swipe = jsonable_encoder(swipe)
    resp = requests.post(f"{SWIPES_URL}/swipes", json=swipe)
    return JSONResponse(content=resp.json(), status_code=resp.status_code)
