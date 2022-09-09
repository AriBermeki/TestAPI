from pydantic import BaseModel
from typing import Optional, Any
from sqlalchemy import create_engine


class Syndicate(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)