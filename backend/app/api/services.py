from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse
from app.core.dependencies import get_current_admin
from app.models.user import User

router = APIRouter(prefix="/api/services", tags=["Services"])


@router.get("/", response_model=list[ServiceResponse])
def get_services(db: Session = Depends(get_db)):
    return db.query(Service).filter(Service.is_active == True).all()


@router.get("/{slug}", response_model=ServiceResponse)
def get_service(slug: str, db: Session = Depends(get_db)):
    service = (
        db.query(Service)
        .filter(Service.slug == slug, Service.is_active == True)
        .first()
    )

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    return service


@router.post("/", response_model=ServiceResponse)
def create_service(
    service_data: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):
    existing_service = (
        db.query(Service).filter(Service.slug == service_data.slug).first()
    )

    if existing_service:
        raise HTTPException(
            status_code=400, detail="Service with this slug already exists"
        )

    service = Service(**service_data.model_dump())

    db.add(service)
    db.commit()
    db.refresh(service)

    return service


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(
    service_id: int,
    service_data: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    for key, value in service_data.model_dump().items():
        setattr(service, key, value)

    db.commit()
    db.refresh(service)

    return service


@router.delete("/{service_id}")
def delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin),
):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    db.delete(service)
    db.commit()

    return {"message": "Service deleted successfully"}
