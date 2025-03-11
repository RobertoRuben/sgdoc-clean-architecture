from abc import ABC, abstractmethod
from src.application.dto import (
    DocumentaryDomainRequestDTO,
    DocumentaryDomainResponseDTO,
    PageDocumentaryDomainResponseDTO,
)

class DocumentayUseCase(ABC):

    @abstractmethod
    async def add_documentary_domain(
        self, documentary_domain: DocumentaryDomainRequestDTO
    ) -> DocumentaryDomainResponseDTO:
        """ """
        pass


    @abstractmethod
    async def get_documentary_domains(
        self, page: int, size: int
    ) -> PageDocumentaryDomainResponseDTO:
        """ """
        pass


    @abstractmethod
    async def update_documentary_domain(
        self,
        documentary_domain_id: int,
        documentary_domain: DocumentaryDomainRequestDTO,
    ) -> DocumentaryDomainResponseDTO:
        """ 
        """
        pass
    
    
    @abstractmethod
    async def delete_documentary_domain(self, documentary_domain_id: int) -> None:
        """ """
        pass
    
    
    @abstractmethod
    async def find_documentary_domain(
        self, page: int, size: int, search_dict: dict[str, str]
    ) -> PageDocumentaryDomainResponseDTO:
        """ """
        pass
    
    
    @abstractmethod
    async def get_documentary_domain_by_id(self, documentary_domain_id: int) -> DocumentaryDomainResponseDTO:
        """ """
        pass
