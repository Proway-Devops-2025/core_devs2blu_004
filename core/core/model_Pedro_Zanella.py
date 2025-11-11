from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from core.core.DATABASE.base_class import Base  # ajuste se necessário ao path real

class PedroZanella(Base):
    __tablename__ = "pedro_zanella"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Novas propriedades
    nome = Column(String(100))
    cep = Column(String(9))
    rua = Column(String(200))


