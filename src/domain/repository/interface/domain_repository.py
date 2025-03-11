from abc import ABC, abstractmethod
from src.domain.entity import DocumentaryDomain, Page


class DomainRepository(ABC):
    """
    Interface for the Domain repository
    """

    @abstractmethod
    async def add(self, domain: DocumentaryDomain) -> DocumentaryDomain:
        """
        Add a domain to the repository

        :param domain: Domain object
        :return: Domain object
        """
        pass

    @abstractmethod
    async def get_paginated(self, page: int, size: int) -> Page:
        """
        Get paginated domains

        :param page: Page number
        :param size: Page size
        :return: Page object
        """
        pass

    @abstractmethod
    async def update(self, domain: DocumentaryDomain) -> DocumentaryDomain:
        """
        Update a domain in the repository

        :param domain: Domain object
        :return: Domain object
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
        Find tenants based on partial matches in specified fields

        :param page: Page number
        :param size: Items per page
        :param search_dict: Dictionary with field names as keys and search terms as values
        :return: Page object containing matching tenants
        """
        pass

    @abstractmethod
    async def get_by_id(self, tenant_id: int) -> Page:
        """
        Get a tenant by its ID.

        :param tenant_id: ID of the tenant to retrieve.
        :return: Tenant object with the specified ID.
        """
        pass

    @abstractmethod
    async def exists_by(self, **kwargs) -> bool:
        """
        Check if a tenant exists based on specified criteria.

        :param kwargs: Criteria for checking tenant existence.
        :return: True if a tenant exists, False otherwise.
        """
        pass
