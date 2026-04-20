# IMPORTS
from pydantic import BaseModel
from app.ats_agent import calculate_score 
from fastapi import FastAPI
from app.db import engine
from app.models import Base, Candidate
from app.database import SessionLocal

Base.metadata.create_all(bind=engine)

class ATSRequest(BaseModel):
    name: str
    email: str
    resume_text: str
    job_description: str

app = FastAPI()

# EXISTING API
@app.get("/")
def home():
    return {"message": "Backend is running"}

# ATS API (main feature)
@app.post("/ats-score")
def ats_score(data: ATSRequest):
    db = SessionLocal()

    score = calculate_score(data.resume_text, data.job_description)

    stage = "INTERVIEW" if score >= 80 else "REJECTED"

    candidate = Candidate(
        name=data.name,
        email=data.email,
        resume_text=data.resume_text,
        ats_score=score,
        stage=stage
    )

    db.add(candidate)
    db.commit()
    db.close()

    return {
        "score": score,
        "stage": stage
    }

# ADD API TEST
@app.get("/add")
def add_data():
    db = SessionLocal()

    candidate = Candidate(
        name="Prajwal",
        email="test@gmail.com",
        resume_text="python java sql",
        ats_score=85,
        stage="INTERVIEW"
    )

    db.add(candidate)
    db.commit()
    db.close()

    return {"message": "Data inserted"}
