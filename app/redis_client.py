import os
import redis
from dotenv import load_dotenv

load_dotenv()

try:
    redis_client = redis.from_url(
        os.getenv("REDIS_URL"), # type: ignore
        decode_responses=True
    )
    redis_client.ping()

except Exception:
    redis_client = None