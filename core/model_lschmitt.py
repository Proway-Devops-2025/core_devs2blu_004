from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from core.core.DATABASE.base_class import Base  # ajuste se necessário ao path real

class LeonardoSchmitt(Base):
    __tablename__ = "leonardo_schmitt"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
