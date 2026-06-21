from fastapi import FastAPI , Depends , HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .database_generation import Base , engine,get_db
from .schemas import URLcreate, URLStats
from sqlalchemy.orm import Session

from .crud import create_shorten_url , get_original_url ,get_url_stats

import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv(
    'BASE_URL',
    "http://localhost:8000"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://url-shortner-amber-three.vercel.app',
        'https://url-shortner-git-main-enky-yys-projects.vercel.app',
        'https://url-shortner-1ka4m6owu-enky-yys-projects.vercel.app',
        'https://url-shortner-enky-yys-projects.vercel.app',
        'http://localhost:5173'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*'],
)

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return{
        "message" :'url shortner'
    }

@app.post("/shorten")
def shorten(
    data: URLcreate,
    db :Session=Depends(get_db)):

    url = create_shorten_url(db, str(data.url))

    return {
        'shorten_url': f'{base_url}/{url.short_code}'
    }


@app.get("/{short_code}")
def redirect_to_url(
    short_code: str,
    db: Session = Depends(get_db)):

    
    original_url = get_original_url(db=db, shorten_url= short_code)

    if not original_url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    return RedirectResponse(
        url=original_url, # pyright: ignore[reportArgumentType]
        status_code=301,
    )

@app.get('/stats/{short_code}', response_model=URLStats)
def stats(short_code :str, db:Session=Depends(get_db)):
    url = get_url_stats(db,short_code)

    if not url:
        raise HTTPException(
            status_code=404,
            detail='URL not found'
        )
    
    return{
        'original_url': url.original_url,
        'short_code' : url.short_code,
        'clicks' : url.clicks
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }