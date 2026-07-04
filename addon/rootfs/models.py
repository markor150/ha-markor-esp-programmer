from pydantic import BaseModel

class FlashRequest(BaseModel):
    firmware: str
