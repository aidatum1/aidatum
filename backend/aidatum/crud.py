from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas

def get_recall(db: Session, recall_id: int) -> Optional[models.Recall]:
    """Get a recall by ID"""
    return db.query(models.Recall).filter(models.Recall.id == recall_id).first()

def get_recalls(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    manufacturer: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[models.RecallStatus] = None,
) -> List[models.Recall]:
    """Get recalls with optional filters"""
    query = db.query(models.Recall)
    
    if manufacturer:
        query = query.filter(models.Recall.manufacturer == manufacturer)
    if product_type:
        query = query.filter(models.Recall.product_type == product_type)
    if status:
        query = query.filter(models.Recall.status == status)
    
    return query.offset(skip).limit(limit).all()

def create_recall(db: Session, recall: schemas.RecallCreate) -> models.Recall:
    """Create a new recall"""
    db_recall = models.Recall(**recall.model_dump())
    db.add(db_recall)
    db.commit()
    db.refresh(db_recall)
    return db_recall

def update_recall(
    db: Session, recall_id: int, recall: schemas.RecallUpdate
) -> Optional[models.Recall]:
    """Update a recall"""
    db_recall = get_recall(db, recall_id)
    if not db_recall:
        return None
    
    update_data = recall.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_recall, field, value)
    
    db_recall.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_recall)
    return db_recall

def delete_recall(db: Session, recall_id: int) -> bool:
    """Delete a recall"""
    db_recall = get_recall(db, recall_id)
    if not db_recall:
        return False
    
    db.delete(db_recall)
    db.commit()
    return True