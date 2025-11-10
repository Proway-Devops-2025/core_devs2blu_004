"""
Module for the BryanPacker model.

This module contains the BryanPacker data model definition.
"""
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from core.core.DATABASE.base_class import Base


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