from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.lead import Lead
from app.schemas.lead import LeadCreate, LeadResponse
from app.core.dependencies import get_current_user
from app.models.user import User 


router = APIRouter(prefix="/api/leads", tags=["Leads"])


@router.post("/", response_model=LeadResponse)
def create_lead(lead_data: LeadCreate, db: Session = Depends(get_db)):
    lead = Lead(**lead_data.model_dump())

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead


@router.get("/", response_model=list[LeadResponse])
def get_leads(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Lead).order_by(Lead.created_at.desc()).all()
