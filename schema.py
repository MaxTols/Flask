from typing import Optional
from pydantic import BaseModel, validator


class CreateUser(BaseModel):
    name: str
    password: str

    @validator("password")
    def password_verification(cls, value):
        if len(value) <= 6:
            raise ValueError("Password is short")
        return value


class UpdateUser(BaseModel):
    name: Optional[str]
    password: Optional[str]

    @validator("password")
    def password_verification(cls, value):
        if len(value) <= 6:
            raise ValueError("Password is short")
        return value
