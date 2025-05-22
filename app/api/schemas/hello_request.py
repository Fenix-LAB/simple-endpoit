from pydantic import BaseModel, Field


class HelloRequest(BaseModel):
    name: str = Field(..., description="Name of the user")
