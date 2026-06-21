from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database_generation import Base

class URL(Base):
    __tablename__ = 'url_data'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    original_url = Column(
        String,
        nullable= False
    )
    short_code = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    click = Column(
        Integer,
        default=0
    )