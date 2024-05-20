from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class Message(Base):
    __tablename__ = "message"

    index = Column(Integer, primary_key=True)
    first_message = Column(String)
    second_message = Column(String)
    third_message = Column(String)
