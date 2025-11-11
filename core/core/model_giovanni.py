from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from core.core.DATABASE.base_class import Base  # ajuste o caminho se necessário


class Giovanni(Base):
    __tablename__ = "giovanni"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

