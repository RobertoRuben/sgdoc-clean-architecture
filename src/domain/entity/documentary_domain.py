from dataclasses import dataclass, Field


@dataclass
class DocumentaryDomain:
    id: int | None
    domain_name: str
