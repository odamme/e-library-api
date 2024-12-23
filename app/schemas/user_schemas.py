from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    first_name:str 
    last_name:str
    email: EmailStr
    password:str
 
class UserStatus(BaseModel):
    is_active:bool = True
              
class User(UserBase, UserStatus):
    id: int = 10001


class CreateUser(UserBase):
    first_name:str = "Damilola"
    last_name:str = "Oladeji"
    email: EmailStr = "oladejidam@gmail.com"
    password:str = "password"
    confirm_password:str = "password"
    
class UserLogin(BaseModel):
    username:str = "oladejidam@gmail.com"
    password:str = "password"
        
class UpdateUser(BaseModel):
    first_name:Optional[str] = "Damilola"
    last_name:Optional[str] = "Oladeji"
    
class ChangePassword(BaseModel):
    old_password:str = "password"
    new_password:str = "password_new"
    confirm_password:str = "password_new" 