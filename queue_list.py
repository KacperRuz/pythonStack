from typing import Any
from linked_list import LinkedList

class Queue:
    def __init__(self) -> None:
        self.storage = LinkedList()

    def __str__(self) -> str:
        return self.storage.__str__()

    def __len__(self) -> int:
        return self.storage.size

    def peek(self) -> Any:
        return self.storage.data.value

    def enqueue(self, value: Any) -> None:
        self.storage.append(value)

    def dequeue(self) -> Any:
        return self.storage.pop()
