from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

Base = declarative_base()


class Meeting(Base):

    __tablename__ = "meetings"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(String)

    company = Column(String)

    domain = Column(String)

    attendees = Column(Text)

    meeting_time = Column(String)

    brief = Column(Text)