from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.database.database import Base


class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(30))

    audience = Column(String(30), nullable=False)
    service = Column(String(150))

    preferred_date = Column(String(50))
    preferred_time = Column(String(50))

    message = Column(Text)

    status = Column(String(30), default="pending", nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
