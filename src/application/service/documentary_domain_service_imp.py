from src.domain.service.interface import DomainService
from src.domain.repository.interface import DomainRepository
from src.domain.entity import DocumentaryDomain, Page

class DocumentaryDomainServiceImpl(DomainService):
    """
    Implementation of the Domain Service
    """
    
    def __init__(self, repository: DomainRepository):
        """
        Initialize the service with a repository
        
        :param repository: Repository implementation
        """
        self.repository = repository
    
    
    async def add_documentary_domain(self, domain: DocumentaryDomain) -> DocumentaryDomain:
        """
        Add a new domain
        
        :param domain: Domain to add
        :return: Added domain with generated ID
        """
        return await self.repository.add(domain)
    
    
    async def get_paginated_documentary_domains(self, page: int, size: int) -> Page:
        """
        Get domains with pagination
        
        :param page: Page number
        :param size: Page size
        :return: Page object with domains
        """
        return await self.repository.get_paginated(page, size)
    
    
    async def update(self, domain: DocumentaryDomain) -> DocumentaryDomain:
        """
        Update an existing domain
        
        :param domain: Domain with updated values
        :return: Updated domain
        """
        return await self.repository.update(domain)
    
    
    async def delete(self, domain_id: int) -> bool:
        """
        Delete a domain by ID
        
        :param domain_id: Domain ID to delete
        :return: True if successful, False otherwise
        """
        return await self.repository.delete(domain_id)
    
    
    async def find(self, page: int, size: int, search_dict: dict[str, str]) -> Page:
        """
        Find domains based on search criteria
        
        :param page: Page number
        :param size: Page size
        :param search_dict: Search criteria
        :return: Page object with matching domains
        """
        return await self.repository.find(page, size, search_dict)
    
    
    async def get_by_id(self, domain_id: int) -> DocumentaryDomain:
        """
        Get a domain by its ID
        
        :param domain_id: Domain ID
        :return: Domain object
        """
        return await self.repository.get_by_id(domain_id)