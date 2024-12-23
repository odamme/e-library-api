from schemas.user_schemas import UserBase
from schemas.user_schemas import User
from schemas.user_schemas import UpdateUser
from schemas.user_schemas import ChangePassword
from schemas.user_schemas import UserLogin
from schemas.user_schemas import UserStatus
from schemas.user_schemas import CreateUser
from schemas.user_schemas import UpdateUser
from database.in_memory import users
from fastapi import HTTPException, status

class UserCrud():
    
    @staticmethod
    def create_user(user_data:CreateUser):
        if user_data.password != user_data.confirm_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Password incorrect, please try again")
     
        for id, user_profile in users.items():
            if user_profile.email == user_data.email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
            
        user_id = len(user_data.first_name) + len(user_data.last_name) + len(user_data.email) + 10000
        
        user = User( id=user_id, **user_data.model_dump())
   
        users[user_id] = user
        return user
    
    @staticmethod
    def get_user_by_id(user_id:int):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        return user
        
               
    @staticmethod
    def user_login(user:UserLogin):
        for id, user_profile in users.items():
            if user_profile.email != user.username:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Email Address")
            if user_profile.password != user.password:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    
            return "Login Successful"
        
    @staticmethod
    def get_users():
        return users
    
    @staticmethod
    def update_user(user_id:int, user_data:UpdateUser):
        user:User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        for id, user_profile in user_data.model_dump(exclude_unset=True).items():
            setattr(user, id, user_profile)
            
        return user
       
    @staticmethod
    def delete_user(user_id:int):
        user:User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        del users[user_id] 
        return
    
user_crud = UserCrud()