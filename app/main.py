from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"status": "Backend running"}


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    return crud.create_user(db, user)


@app.post("/login")
def login(user: schemas.UserLogin, response: Response, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user.username, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    response.set_cookie(
        key="session",
        value=str(db_user.id),
        httponly=True,
        samesite="lax"
    )

    return {"message": "Login successful"}
