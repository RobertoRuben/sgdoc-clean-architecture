from pydantic import BaseModel

class DocumentaryDomainResponseDTO(BaseModel):
    id: int
    domain_name: str
    
    
class PageDocumentaryDomainResponseDTO(BaseModel):
    total_items: int
    total_pages: int
    page: int
    size: int
    items: list[DocumentaryDomainResponseDTO]
    