from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from core.core.DATABASE.base_class import Base  # ajuste se necessário ao path real

class GuilhermeCavaco(Base):
    __tablename__ = "guilherme_cavaco"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

numeros = [1, 2, 3, 4] ## Numeross a serem elevados ao quadrado
quadrados = [] ## Lista para armazenar os quadrados
for n in numeros:  ## Loop através dos números
    quadrados.append(n ** 2) ## Adiciona o quadrado do número à lista
print(quadrados) ## Imprime a lista de quadrados