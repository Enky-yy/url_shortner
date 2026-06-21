from pydantic import BaseModel

class URLcreate(BaseModel):
    url:str

class URLShortner(BaseModel):
    url_shorten : str