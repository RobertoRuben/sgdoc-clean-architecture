from typing import Any
from dataclasses import dataclass

@dataclass
class Page:
    total_items: int
    total_pages: int
    page: int
    size: int
    items: list[Any]