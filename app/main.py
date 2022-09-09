import os
from .model import AccountModel
from .schema import AccountSchema, UpdateAccountSchema
from typing import Optional, List
import asyncio
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import Response
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
from .oauth import AuthHandler
from .oauth_schema import OAuthDetails
from .create import create_router
from .read import read_router
from .delete import delete_router
from .update import update_router
from .email import email_router




app = FastAPI(
    title="GoQuanto is a Scientific  Platform",
    description="Mathematics----Physics----Chemistry",
    version="0.0.1",
    contact={
        "Organisation Name":"GoQuanto is a Scientific  Platform",
        "CTO Email": 'ari.bermeki@icloud.com',
        "Organisation Address":"Germany, Berlin"
    },
    license_info={
        "name":"MIT"
    }
)




app.include_router(create_router)
app.include_router(read_router)
app.include_router(delete_router)
app.include_router(update_router)
app.include_router(email_router)




    


    









   
