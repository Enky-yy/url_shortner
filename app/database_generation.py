from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL= 'sqlite:///./url_data.db'

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread':False}
)

sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()