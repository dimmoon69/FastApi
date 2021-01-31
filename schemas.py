from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class UploadUserFile(BaseModel):
    title: str
    description: str


class GetUserFile(BaseModel):
    user: User
    file: UploadUserFile