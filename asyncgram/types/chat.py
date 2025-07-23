from pydantic import BaseModel

class Chat(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    type: str



