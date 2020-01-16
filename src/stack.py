from node import Node
from typing import Optional, Any, Generic, TypeVar, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, *args: T) -> None:
        self.top: Optional[Node[T]] = None
        if args is not None:
            for arg in args:
                self.push(arg)

    def push(self, data: T) -> None:
        self.top = Node(data=data, prev=self.top)

    def pop(self) -> Optional[T]:
        data: Optional[T]
        if self.is_Empty():
            data = None
        else:
            data = self.top.data
            self.top = self.top.prev
        return data

    def is_empty(self) -> bool:
        return True if self.top is None else False

    def get_state(self) -> list:
        current: Optional[Node[T]] = self.top
        trace: List = []
        while current is not None:
            trace.append(current.data)
            current = current.prev
        trace = trace[::-1]
        return trace
