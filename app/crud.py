import random
import string

from sqlalchemy.orm import Session

from .db_models import URL

def generate_rnd_code(length=6):
    chars = string.ascii_letters + string.digits

    return "".join(
        random.choice(chars) for _ in range(length)
    )

def create_shorten_url(db:Session, original_url:str):

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

# def redirects(db:Session, shorten_url: str):
