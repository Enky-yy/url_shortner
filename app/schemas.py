from pydantic import BaseModel, HttpUrl

class URLcreate(BaseModel):
    url:HttpUrl

class URLShortner(BaseModel):
    url_shorten : str

class URLStats(BaseModel):
    original_url: str
    short_code: str
    clicks: int