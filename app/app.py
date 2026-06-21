from fastapi import FastAPI , Depends , HTTPException
from fastapi.responses import RedirectResponse

from .database_generation import Base , engine,get_db
from .schemas import URLcreate, URLShortner
from sqlalchemy.orm import Session

from .crud import create_shorten_url , get_original_url

app = FastAPI()

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

    url = create_shorten_url(db, data.url)

    return {
        'shorten_url': f'http://localhost:8000/{url.short_code}'
    }

# @app.get("/{short_code}")
# def redirects(short_code : URLShortner , db:Session=Depends(get_db)):
#     url = get_shorten_url(db=db, short_code.url_shorten)


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
        url=original_url
    )