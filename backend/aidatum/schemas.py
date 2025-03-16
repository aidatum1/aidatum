from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from .models import RecallStatus

class RecallBase(BaseModel):
    """Base schema for Recall"""
    title: str
    description: str
    manufacturer: str
    product_type: str
    status: RecallStatus
    recall_date: datetime

class RecallCreate(RecallBase):
    """Schema for creating a recall"""
    pass

class Recall(RecallBase):
    """Schema for recall response"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RecallUpdate(BaseModel):
    """Schema for updating a recall"""
    title: Optional[str] = None
    description: Optional[str] = None
    manufacturer: Optional[str] = None
    product_type: Optional[str] = None
    status: Optional[RecallStatus] = None
    recall_date: Optional[datetime] = None