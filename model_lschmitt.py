from sqlalchemy import Column, String

class LeonardoSchmitt(Base):
    __tablename__ = "maria_silva"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Novas propriedades
    nome = Column(String(100))
    cep = Column(String(9))
    rua = Column(String(200))
