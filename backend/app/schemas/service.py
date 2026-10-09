from pydantic import BaseModel
from typing import Optional


class ServiceBase(BaseModel):
    name: str
    slug: str
    short_description: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True
