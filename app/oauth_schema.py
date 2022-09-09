from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
import datetime  



class OAuthDetails(BaseModel):

    username: str
    password: str

    class Config:
        orm_mode=True