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



update_router = APIRouter()

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

#update_router.mount("/static", StaticFiles(directory="static"), name="static")


@update_router.put('/update_user/{user_id}', status_code=status.HTTP_202_ACCEPTED)
async def User_delete_ByID(user_update:UpdateAccountSchema,user_id: int):
    for item in datasystem:

        if item.id == user_id:

            if user_update.frist_name is not None:
                item.frist_name = user_update.frist_name

            if user_update.last_name is not None:
                item.last_name = user_update.last_name

            if user_update.email is not None:
                item.email = user_update.email

            if user_update.username is not None:
                item.username = user_update.username

            if user_update.date_joined is not None:
                item.date_joined = user_update.date_joined

            if user_update.last_login is not None:
                item.last_login = user_update.last_login

            if user_update.password is not None:
                item.password = user_update.password

            if user_update.confirm_password is not None:
                item.confirm_password = user_update.confirm_password

            if user_update.role is not None:
                item.role = user_update.role
            return 


    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"This User with that identification ID-Nummber: {user_id} does not exist"
    ) 