from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T, prev=None):
        self.data: T = data
        self.prev = prev
