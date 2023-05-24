import os
from sqlalchemy import create_engine,Column,Integer,ForeignKey,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import uuid4



POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')


SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres_db/{POSTGRES_DB}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True,nullable=False)
    token = Column(String,unique=True,nullable=False)

    def __init__(self,username):
        self.username = username
        self.token = str(uuid4())

    def __repr__(self) -> str:
        return f'User {self.username}'


class AudioRecord(Base):
    __tablename__ = 'audio_records'

    id  = Column(String,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    filename = Column(String,unique=True,nullable=False)