from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import firebase_admin
from firebase_admin import credentials, auth
import json
from dotenv import load_dotenv
import os

firebasekey = json.loads(os.getenv("FIREBASE_KEY"))
cred = credentials.Certificate(firebasekey)

firebase = firebase_admin.initialize_app(cred)

security = HTTPBearer()


async def get_current_user(token: Annotated[str, Depends(security)]):
    user = auth.verify_id_token(token.credentials)
    print(user)
    if user:
        return user
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
