from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import get_db

router = APIRouter()

@router.get("/recalls/", response_model=List[schemas.Recall])
def read_recalls(
    skip: int = 0,
    limit: int = 100,
    manufacturer: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[models.RecallStatus] = None,
    db: Session = Depends(get_db),
):
    """Get list of recalls with optional filters"""
    recalls = crud.get_recalls(
        db,
        skip=skip,
        limit=limit,
        manufacturer=manufacturer,
        product_type=product_type,
        status=status,
    )
    return recalls

@router.get("/recalls/{recall_id}", response_model=schemas.Recall)
def read_recall(recall_id: int, db: Session = Depends(get_db)):
    """Get a specific recall by ID"""
    db_recall = crud.get_recall(db, recall_id=recall_id)
    if db_recall is None:
        raise HTTPException(status_code=404, detail="Recall not found")
    return db_recall

@router.post("/recalls/", response_model=schemas.Recall)
def create_recall(recall: schemas.RecallCreate, db: Session = Depends(get_db)):
    """Create a new recall"""
    return crud.create_recall(db=db, recall=recall)

@router.patch("/recalls/{recall_id}", response_model=schemas.Recall)
def update_recall(
    recall_id: int, recall: schemas.RecallUpdate, db: Session = Depends(get_db)
):
    """Update a recall"""
    db_recall = crud.update_recall(db=db, recall_id=recall_id, recall=recall)
    if db_recall is None:
        raise HTTPException(status_code=404, detail="Recall not found")
    return db_recall

@router.delete("/recalls/{recall_id}")
def delete_recall(recall_id: int, db: Session = Depends(get_db)):
    """Delete a recall"""
    success = crud.delete_recall(db=db, recall_id=recall_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recall not found")
    return {"message": "Recall deleted successfully"}