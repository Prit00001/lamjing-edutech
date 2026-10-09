from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.consultation import Consultation
from app.schemas.consultation import ConsultationCreate, ConsultationResponse
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/consultations", tags=["Consultations"])


@router.post("/", response_model=ConsultationResponse)
def create_consultation(
    consultation_data: ConsultationCreate, db: Session = Depends(get_db)
):
    consultation = Consultation(**consultation_data.model_dump())

    db.add(consultation)
    db.commit()
    db.refresh(consultation)

    return consultation


@router.get("/", response_model=list[ConsultationResponse])
def get_consultations(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return db.query(Consultation).order_by(Consultation.created_at.desc()).all()
