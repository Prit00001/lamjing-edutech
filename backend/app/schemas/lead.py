from pydantic import BaseModel, EmailStr
from typing import Optional


class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    audience: str
    service: Optional[str] = None
    message: Optional[str] = None


class LeadResponse(LeadCreate):
    id: int

    class Config:
        from_attributes = True
