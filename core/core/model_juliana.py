from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from core.core.DATABASE.base_class import Base


class Juliana(Base):
    __tablename__ = "juliana"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)