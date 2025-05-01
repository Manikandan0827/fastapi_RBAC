from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import User
from schemas import UserCreate, Token,UserLogin, Message
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=Message,status_code=201)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    user_exists = session.exec(select(User).where(User.username == user_data.username)).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")

    user = User(
        username=user_data.username,
        hashed_password=hash_password(user_data.password),
        role=user_data.role
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == user_data.username)).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}
