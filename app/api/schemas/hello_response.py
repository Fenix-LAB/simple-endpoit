from pydantic import BaseModel, Field


class HelloResponse(BaseModel):
    message: str = Field(..., description="Message of the response")
    