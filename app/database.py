from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DTABASE = "sqlite:///" + os.path.join(BASE_DIR, 'ari.db')
engine = create_engine(DTABASE, echo = True, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine,  future=True)
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()