from typing import Annotated
from dotenv import load_dotenv
import os
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
import requests
from ..middleware.firebase import get_current_user


router = APIRouter(
    prefix="/recommendations",
    tags=['Recommendations'],
    dependencies=[Depends(get_current_user)]
)


load_dotenv()
RECOMMENDATIONS_URL = os.getenv("RECOMMENDATIONS_URL")


@router.get('/')
def get_recommendations(
        current_user: Annotated[dict, Depends(get_current_user)]):
    """
    Get Some Recommendations from Users Dtabase.
    """
    user_id = current_user["uid"]
    resp = requests.get(f"{RECOMMENDATIONS_URL}/recommendations/{user_id}")
    return JSONResponse(content=resp.json(), status_code=resp.status_code)
