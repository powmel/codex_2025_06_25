# Mentor Matching App

This repository contains a minimal FastAPI backend implementing part of the "AI-Personalized Mentor Matching Platform for Programming" concept.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000/`.

## Available Endpoints

- `POST /users/` – create a user (student or teacher).
- `POST /teacher_profiles/` – create a teacher profile linked to a user.
- `POST /curriculums/` – create a curriculum for a student.

These are initial endpoints and serve as a foundation for further development of the matching platform.
