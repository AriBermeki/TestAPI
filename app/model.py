import enum
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime, Date,Boolean,Enum, Text
from sqlalchemy.orm import relationship
from .database import Base
from .mixins_model import Timestamp
from datetime import datetime

#from sqlalchemy_utils import URLType


class Role(enum.Enum):
    is_admin               = 1
    is_superuser           = 2


class AccountModel(Timestamp, Base):

   __tablename__ = 'Accountes'
   id                     = Column(Integer, primary_key = True)
   frist_name             = Column(String)                                    
   last_name              = Column(String) 
   email                  = Column(String)                                    
   username               = Column(String)     
   last_login             = Column(String)
   data_joined            = Column(String)
   password               = Column(String)
   confirm_password       = Column(String)
   role                   = Column(Enum(Role))
   

   def __repr__(self):
      return f"<Accountes id={self.id} frist_name={self.frist_name} last_name={self.last_name}email={self.email} username={self.username} last_login={self.last_login} data_joined={self.data_joined} password={self.password} confirm_password={self.confirm_password}"
 

   
