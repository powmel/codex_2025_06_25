from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mentor Matching API")

# Dependency to get DB session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/teacher_profiles/", response_model=schemas.TeacherProfile)
def create_profile(profile: schemas.TeacherProfileCreate, db: Session = Depends(get_db)):
    return crud.create_teacher_profile(db, profile)

@app.post("/curriculums/", response_model=schemas.Curriculum)
def create_curriculum(curriculum: schemas.CurriculumCreate, db: Session = Depends(get_db)):
    return crud.create_curriculum(db, curriculum)

@app.get("/")
def read_root():
    return {"message": "Mentor Matching API"}

