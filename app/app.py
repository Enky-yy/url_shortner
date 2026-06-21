from fastapi import FastAPI , Depends

from .database_generation import Base , engine,get_db
from .schemas import URLcreate, URLShortner
from sqlalchemy.orm import Session

from .crud import create_shorten_url

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return{
        "message" :'url shortner'
    }

@app.get('/shorten')
def shorten(
    data: URLcreate,
    db :Session=Depends(get_db)):

    url = create_shorten_url(db, data.url)

    return {
        'shorten_url': f'http;//localhost:8000/{url.short_code}'
    }

