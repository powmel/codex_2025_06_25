from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Users

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Teacher profile

def create_teacher_profile(db: Session, profile: schemas.TeacherProfileCreate) -> models.TeacherProfile:
    db_profile = models.TeacherProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

# Curriculum

def create_curriculum(db: Session, curriculum: schemas.CurriculumCreate) -> models.Curriculum:
    db_curriculum = models.Curriculum(
        student_id=curriculum.student_id,
        roadmap=curriculum.roadmap,
        created_at=datetime.utcnow(),
    )
    db.add(db_curriculum)
    db.commit()
    db.refresh(db_curriculum)
    return db_curriculum

