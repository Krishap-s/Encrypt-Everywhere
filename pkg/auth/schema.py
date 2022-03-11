from pydantic import BaseModel, EmailStr

class AddUserSchema(BaseModel):
    name:str
    email:EmailStr
    salt:str
    encrypted_master_password:str
    derived_key:str

class SignInSchema(BaseModel):
    email:EmailStr
    derived_key:str