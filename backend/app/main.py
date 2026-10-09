from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.database.database import Base, engine
from app.models.service import Service
from app.api.services import router as services_router
from app.models.lead import Lead
from app.api.leads import router as leads_router
from app.models.consultation import Consultation
from app.schemas.consultation import ConsultationCreate, ConsultationResponse
from app.api.consultations import router as consultations_router
from app.models.user import User
from app.api.auth import router as auth_router
from app.core.security import verify_password, create_access_token

# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lamjing Edutech API",
    description="API for Lamjing Edutech",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(services_router, prefix="/services", tags=["Services"])
app.include_router(leads_router, prefix="/leads", tags=["Leads"])
app.include_router(
    consultations_router, prefix="/consultations", tags=["Consultations"]
)
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
def root():
    return {
        "message": "Welcome to Lamjing Edutech API",
        "endpoints": {
            "/services": "Get all services",
            "/services/{service_id}": "Get a service by ID",
            "/leads": "Get all leads",
            "/consultations": "Get all consultations",
            "/auth/login": "Login to the API",
        },
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
