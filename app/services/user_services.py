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
from crud.users import users

class UserService():
     
    @staticmethod
    def change_password(user_id:int, user_data:ChangePassword):
        user:User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        for id, user_profile in users.items():
            if user_profile.password != user_data.old_password:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
            if user_data.new_password != user_data.confirm_password:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "The passwords provided do not match. Please try again.")

            user_profile.password = user_data.new_password
        return user
    
  
    @staticmethod
    def deactivate_user(user_id:int):
        user:User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        if user.is_active != True:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already deactivated")
            
        user.is_active = False
        
        return
    
    @staticmethod
    def validate_active_user(user_id:int):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        if user.is_active == True:
                return True
        return False
user_service = UserService()