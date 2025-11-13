from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, Date, Time
from core.core.DATABASE.base_class import Base  

class Joinville(Base):
    __tablename__ = "joinville"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    type = Column(String(50), nullable=False)


class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    
    # Informações básicas
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(500))
    
    # Data e hora
    data = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fim = Column(Time)