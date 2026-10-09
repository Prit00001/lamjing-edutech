from pydantic import BaseModel,EmailStr
from typing import Optional


class ConsultationCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    audience: str
    service: Optional[str] = None
    preferred_date: Optional[str] = None
    preferred_time: Optional[str] = None
    message: Optional[str] = None


class ConsultationResponse(ConsultationCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
