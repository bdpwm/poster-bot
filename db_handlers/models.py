from sqlalchemy import Column, Integer, String, BigInteger, TIMESTAMP, TEXT, DATE, Boolean
from sqlalchemy.ext.declarative import declarative_base
from utils.utils import get_now_time

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    content = Column(TEXT, nullable=False)
    photo_path = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=get_now_time())
    status = Column(String(50), default='pending')
    approved_at = Column(TIMESTAMP, nullable=True)
