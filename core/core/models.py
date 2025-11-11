from sqlalchemy import Column, String

class MariaSilva(Base):
    __tablename__ = "marcio_ramos"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Novas propriedades
    nome = Column(String(100))
    cep = Column(String(9))
    rua = Column(String(200))
