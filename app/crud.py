import random
import string

from sqlalchemy.orm import Session

from .db_models import URL

from.redis_client import redis_client

def generate_rnd_code(length=6):
    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars) for _ in range(length)
    )

def create_shorten_url(db:Session, original_url:str):

    existing_url = db.query(URL).filter(URL.original_url==original_url).first()

    if existing_url:
        return existing_url

    while True:

        code = generate_rnd_code(6)

        if_existing = (
            db.query(URL).filter(URL.short_code==code).first()
        )

        if not if_existing:
            break
    
    url = URL(original_url= original_url, short_code = code)

    db.add(url)
    db.commit()
    db.refresh(url)

    return url

def get_original_url(db:Session, shorten_url: str):


    if redis_client:
        cached_url = redis_client.get(shorten_url)

        if cached_url:
            print('cache hit')
            url =(db.query(URL).filter(URL.short_code==shorten_url).first())

            if url:
                url.clicks +=1
                db.commit()
        
            return cached_url
    
    print('cache miss')
    
    url =(db.query(URL).filter(URL.short_code==shorten_url).first())

    if not url:
        return None
    

    if redis_client:
        redis_client.set(shorten_url, url.original_url, ex=3600)
    
    url.clicks +=1

    db.commit()

    return url.original_url

def get_url_stats(
    db: Session,
    short_code: str):

    data =(db.query(URL)
        .filter(URL.short_code == short_code)
        .first())

    return (
        data
    )