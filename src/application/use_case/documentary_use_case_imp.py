from .interface.documentary_domain_use_case import DocumentayUseCase
from src.application.dto import (
    DocumentaryDomainRequestDTO,
    DocumentaryDomainResponseDTO,
    PageDocumentaryDomainResponseDTO,
)
from src.domain.service.interface import DomainService
from src.domain.entity import DocumentaryDomain, Page

class DocumentaryUseCaseImpl(DocumentayUseCase):

    def __init__(self, domain_service: DomainService):
        self.domain_service = domain_service
    
    
    async def add_documentary_domain(
        self, documentary_domain: DocumentaryDomainRequestDTO
    ) -> DocumentaryDomainResponseDTO:
        domain = DocumentaryDomain(
            domain_name=documentary_domain.domain_name
        )

        created_domain = await self.domain_service.add_documentary_domain(domain)
        
        return DocumentaryDomainResponseDTO(
            id=created_domain.id,
            domain_name=created_domain.domain_name
        )
    
    
    async def get_documentary_domains(
        self, page: int, size: int
    ) -> PageDocumentaryDomainResponseDTO:
        result_page = await self.domain_service.get_paginated_documentary_domains(page, size)
        
        items_dto = [
            DocumentaryDomainResponseDTO(
                id=domain.id,
                domain_name=domain.domain_name
            ) for domain in result_page.items
        ]
        
        return PageDocumentaryDomainResponseDTO(
            total_items=result_page.total_items,
            total_pages=result_page.total_pages,
            page=result_page.page,
            size=result_page.size,
            items=items_dto
        )
    
    
    async def update_documentary_domain(
        self,
        documentary_domain_id: int,
        documentary_domain: DocumentaryDomainRequestDTO,
    ) -> DocumentaryDomainResponseDTO:

        domain = DocumentaryDomain(
            id=documentary_domain_id,
            domain_name=documentary_domain.domain_name
        )
        
        updated_domain = await self.domain_service.update(domain)
        
        return DocumentaryDomainResponseDTO(
            id=updated_domain.id,
            domain_name=updated_domain.domain_name
        )
    
    
    async def delete_documentary_domain(self, documentary_domain_id: int) -> None:
        result = await self.domain_service.delete(documentary_domain_id)
        
    
    async def find_documentary_domain(
        self, page: int, size: int, search_dict: dict[str, str]
    ) -> PageDocumentaryDomainResponseDTO:

        result_page = await self.domain_service.find(page, size, search_dict)
        
        items_dto = [
            DocumentaryDomainResponseDTO(
                id=domain.id,
                domain_name=domain.domain_name
            ) for domain in result_page.items
        ]
        
        return PageDocumentaryDomainResponseDTO(
            total_items=result_page.total_items,
            total_pages=result_page.total_pages,
            page=result_page.page,
            size=result_page.size,
            items=items_dto
        )
    
    
    async def get_documentary_domain_by_id(self, documentary_domain_id: int) -> DocumentaryDomainResponseDTO:
        domain = await self.domain_service.get_by_id(documentary_domain_id)
        
        return DocumentaryDomainResponseDTO(
            id=domain.id,
            domain_name=domain.domain_name
        )