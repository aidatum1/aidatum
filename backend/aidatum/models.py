from sqlalchemy import Column, Integer, String, DateTime, Text, Enum
from sqlalchemy.sql import func
import enum

from .database import Base

class RecallStatus(str, enum.Enum):
    """Recall status enumeration"""
    ACTIVE = "active"
    COMPLETED = "completed"
    TERMINATED = "terminated"

class Recall(Base):
    """Recall model"""
    __tablename__ = "recalls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    manufacturer = Column(String(255), nullable=False)
    product_type = Column(String(100), nullable=False)
    status = Column(Enum(RecallStatus), default=RecallStatus.ACTIVE)
    recall_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())