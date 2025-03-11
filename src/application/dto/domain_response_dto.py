from pydantic import BaseModel

class DocumentaryDomainResponseDTO(BaseModel):
    id: int
    domain_name: str