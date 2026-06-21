from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import mapped_column , Mapped

from .database_generation import Base

class URL(Base):
    __tablename__ = 'url_data'

    id: Mapped[int]= mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    original_url:Mapped[str]= mapped_column(
        String,
        nullable= False
    )
    short_code:Mapped[str]= mapped_column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    clicks :Mapped[int]= mapped_column(
        Integer,
        default=0
    )