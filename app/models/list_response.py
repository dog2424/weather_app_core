
from typing import Any, List


class ListResponse:

    def __init__(self, items: List[Any], totalItems: int):
        self.items = items
        self.totalItems = totalItems
