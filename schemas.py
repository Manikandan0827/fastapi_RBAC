from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserRead(BaseModel):
    id: int
    username: str
    role: str

class Token(BaseModel):
    access_token: str
    message: str = "login successful"

class ProjectCreate(BaseModel):
    name: str
    description: str

class Message(BaseModel):
    message: str