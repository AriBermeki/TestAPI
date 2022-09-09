import os
from .model import AccountModel
from .schema import AccountSchema, UpdateAccountSchema
from typing import Optional, List
import asyncio
from fastapi import FastAPI, status, Depends, HTTPException, APIRouter
from fastapi.responses import Response
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
from .oauth import AuthHandler
from .oauth_schema import OAuthDetails


create_router = APIRouter()

oauth_handler = AuthHandler()
users = []
BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)
#template = Jinja2Templates(directory= BASE_DIR /"templates")







datasystem:List[AccountSchema] = [
    AccountSchema(
        id= 1,
        frist_name= "Malek",
        last_name="Ali",
        email="ari.bermeki@icloud.com",
        username="ari.bermeki",
        date_joined="09.09.2022",
        last_login="09.09.2022",
        password="323691malek",
        confirm_password="323691malek",
        role= "is_admin"
    )
]


#create_router.mount("/static", StaticFiles(directory="static"), name="static")
@create_router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def create_User(account: AccountSchema):
    new_user = datasystem.append(account)
    return new_user
    