from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    text: str = Field(..., description="Prompt text for the model")


class GenerateResponse(BaseModel):
    response: str = Field(..., description="Model-generated response")
