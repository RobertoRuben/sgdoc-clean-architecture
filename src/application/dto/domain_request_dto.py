from pydantic import BaseModel, Field

class DocumentaryDomainRequestDTO(BaseModel):
    domain_name: str = Field(..., example="example.com", min_length=3)