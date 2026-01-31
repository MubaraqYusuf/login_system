from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user.username, user.password)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    if crud.authenticate_user(db, user.username, user.password):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/profile/{username}", response_model=schemas.UserOut)
def profile(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/delete/{username}")
def delete_account(username: str, db: Session = Depends(get_db)):
    if crud.delete_user(db, username):
        return {"message": "Account deleted"}
    raise HTTPException(status_code=404, detail="User not found")
