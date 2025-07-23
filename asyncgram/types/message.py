from typing import Optional

from pydantic import BaseModel

from asyncgram.types.chat import Chat
from asyncgram.types.user import User


class Message(BaseModel):
    message_id: int
    from_user: Optional[User] = None
    sender_chat: Optional[Chat] = None
