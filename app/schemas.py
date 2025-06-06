from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TeacherProfileBase(BaseModel):
    skills: Optional[str] = None
    experience: Optional[str] = None
    introduction: Optional[str] = None
    rate: Optional[int] = None

class TeacherProfileCreate(TeacherProfileBase):
    user_id: int

class TeacherProfile(TeacherProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class CurriculumBase(BaseModel):
    student_id: int
    roadmap: str

class CurriculumCreate(CurriculumBase):
    pass

class Curriculum(CurriculumBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

