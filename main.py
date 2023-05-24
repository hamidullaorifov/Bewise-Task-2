from fastapi import FastAPI,Depends,HTTPException,status,UploadFile,Request
from pydantic import BaseModel
from sqlalchemy import and_
from sqlalchemy.orm import Session
from database import get_db,Base,engine,User,AudioRecord
from uuid import uuid4
from fastapi.responses import FileResponse



app = FastAPI()
Base.metadata.create_all(engine)


class UserRequest(BaseModel):
    username: str

def get_file_extension(filename):
    if "." in filename:
        extension = filename.split(".")[-1]
        return f".{extension}"
    return ""

@app.post('/users',status_code=status.HTTP_201_CREATED)
def create_user(user: UserRequest,db: Session = Depends(get_db)):
    """Creates a new user in the database."""
    if user.username.isspace() or not user.username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Username cannot be blank')
    
    if db.query(User).filter(User.username==user.username).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Username already exists")
    
    new_user = User(user.username)
    db.add(new_user)
    db.commit()
    return {'id':new_user.id,'token':new_user.token}



@app.post('/audio',status_code=status.HTTP_201_CREATED)
async def save_audio(
        request: Request,
        user_id: int,
        token:str, 
        audio: UploadFile,
        db: Session=Depends(get_db)
    ):
    """Creates a new audio record for a user in the database."""
    user = db.query(User).filter(and_(User.id==user_id,User.token==token)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')

    host =request.headers.get('host')
    filename = audio.filename
    file_extension = get_file_extension(filename)
    
    if file_extension != '.wav':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid file format")
    
    record_id = uuid4()
    mp3_filename = f'{record_id}.mp3'
    
    with open(mp3_filename,'wb') as file:
        content = await audio.read()
        file.write(content)
    
    record = AudioRecord(id=str(record_id),user_id=user_id,filename=mp3_filename)
    db.add(record)
    db.commit()
    
    return {'url': f'{host}/record?id={record_id}&user={user_id}'}



@app.get('/record')
def download_audio(id:str,user:int,db: Session=Depends(get_db)):
    """Downloads an audio file from the database."""
    record = db.query(AudioRecord).filter_by(id=id,user_id=user).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Record not found")
    
    return FileResponse(record.filename,media_type='audio/mp3',filename=record.filename)








