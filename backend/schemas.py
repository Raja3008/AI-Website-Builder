from pydantic import BaseModel


class InitialRequest(BaseModel):
    user_input: str


class ChatInput(BaseModel):
    session_id: str
    message: str