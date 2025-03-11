from abc import ABC, abstractmethod
from src.domain.entity import Domain, Page

class DomainService(ABC):
    """
    Interface for the Domain service
    """
    
    @abstractmethod
    async def add_domain(self, domain: Domain) -> Domain:
        """
        Add a new domain.
        
        :param domain: Domain object
        :return: Created Domain object
        """
        pass
    
    
    @abstractmethod
    async def get_paginated_domains(self, page: int, size: int) -> Page:
        """
        Get paginated domains
        
        :param page: Page number
        :param size: Page size
        :return: Page object with domains
        """
        pass
    
    
    @abstractmethod
    async def update(self, domain: Domain) -> Domain:
        """
        Update a domain in the repository
        
        :param domain: Domain object with updated values
        :return: Updated Domain object
        """
        pass
    
    
    @abstractmethod
    async def delete(self, domain_id: int) -> bool:
        """
        Delete a domain from the repository
        
        :param domain_id: Domain ID
        :return: True if the domain was deleted, False otherwise
        """
        pass
    
    
    @abstractmethod
    async def find(self, page: int, size: int, search_dict: dict[str, str]) -> Page:
        """
        Find domains based on partial matches in specified fields
        
        :param page: Page number
        :param size: Items per page
        :param search_dict: Dictionary with field names as keys and search terms as values
        :return: Page object containing matching domains
        """
        pass
    
    
    @abstractmethod
    async def get_by_id(self, domain_id: int) -> Domain:
        """
        Get a domain by its ID.

        :param domain_id: ID of the domain to retrieve.
        :return: Domain object with the specified ID.
        """
        pass