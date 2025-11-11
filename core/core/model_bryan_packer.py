"""
Module for the BryanPacker models.

This module contains the BryanPacker data models definition.
"""
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from core.core.DATABASE.base_class import Base

from sqlalchemy import Column, String

class BryanPacker(Base):
    """
    Data model for the bryan_packer table.
    
    Attributes:
        id (int): Unique identifier for the record.
        created_at (datetime): Timestamp when the record was created.
    """
    
    __tablename__ = "bryan_packer"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    

class BryanPackerAddress(Base):
    """
    Data model for the bryan_packeraddress table.
    
    Attributes:
        id (int): Unique identifier for the record.
        created_at (datetime): Timestamp when the record was created.
        nome (str): Name, max length 100 characters.
        cep (str): Postal code (CEP), max length 9 characters.
        rua (str): Street address, max length 200 characters.
    """

    __tablename__ = "bryan_packeraddress"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Novas propriedades
    nome = Column(String(100))
    cep = Column(String(9))
    rua = Column(String(200))
