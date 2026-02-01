from sqlalchemy.orm import Session
from . import models
from .auth import hash_password

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, password: str):
    db_user = models.User(
        username=username,
        hashed_password=hash_password(password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, username: str):
    user = get_user(db, username)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
