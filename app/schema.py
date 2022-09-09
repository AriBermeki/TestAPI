from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime  
from enum import Enum
data = datetime



class Role(str,Enum):
    is_admin               = "is_admin"
    is_superuser           = "is_superuser"


class AccountSchema(BaseModel):
    id:Optional [int]
    frist_name: str
    last_name: str
    email : Optional[EmailStr]
    username : str
    date_joined:str
    last_login:str
    password: str
    confirm_password: str
    role: Role

    class Config:
        orm_mode=True


  
class UpdateAccountSchema(BaseModel):
    frist_name: Optional[str]
    last_name: Optional[str]
    email : Optional[EmailStr]
    username : Optional[str]
    date_joined:Optional[str]
    last_login:Optional[str]
    password: Optional[str]
    confirm_password: Optional[str]
    role: Optional[List[Role]]

    class Config:
        orm_mode=True

    