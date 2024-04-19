from typing import Annotated
from fastapi import Depends, HTTPException
import firebase_admin
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import credentials, auth


cred = credentials.Certificate("firebasekey.json")

firebase = firebase_admin.initialize_app(cred)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = auth.verify_id_token(token)
    if user:
        return user["uid"]
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
