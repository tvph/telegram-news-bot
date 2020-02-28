from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer,
                        Sequence, String, DateTime)
from datetime import datetime


# create an engine
engine = create_engine('sqlite:///data.db', echo=True)


# declare a mapping
Base = declarative_base()


# declare the table to hold the infomations
class Info(Base):
    __tablename__ = 'Info'

    id = Column(Integer, Sequence('user_id_seq'), unique=True,
                primary_key=True)
    content = Column(String(200))
    link = Column(String(100))
    date_added = Column(DateTime(), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Info: link - {self.link}, content - {self.content},\
                date added - {self.date_added}'
