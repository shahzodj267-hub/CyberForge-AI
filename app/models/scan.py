from app.models.user import Base

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Scan(Base):

    __tablename__ = "scans"

    id = Column(
        Integer,
        primary_key=True
    )

    scan_type = Column(String)

    target = Column(String)

    result = Column(String)
