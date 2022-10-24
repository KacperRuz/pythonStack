from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    tail: Node
    data: Node  # head
    size: int

    def __init__(self) -> None:
        self.tail = None
        self.data = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        d = self.data
        output = ""
        while True:
            if d is None:
                output = output[:-2]
                break
            else:
                output = output + str(d.value) + "->"
                d = d.next
        return output

    def list(self) -> None:
        d = self.data
        while True:
            if d is None:
                break
            else:
                print(d.value)
                d = d.next

    def node(self, pos: int) -> Node:
        if pos > self.size - 1:
            print("Selected index out of list range.")
            return
        if pos == 0:
            return self.data
        if pos == self.size - 1 and self.tail is not None:
            return self.tail
        d = self.data
        for x in range(0, pos):
            d = d.next
        return d

    def push(self, value: Any) -> None:
        push_node = Node(value)
        if self.data is None:
            self.data = push_node
            self.tail = push_node
            self.size = self.size + 1
            return
        dtemp = self.data
        self.data = push_node
        self.data.next = dtemp
        self.size = self.size + 1

    def pop(self) -> Any:
        if self.size == 0:
            return
        dtemp = self.data
        del self.data
        self.data = dtemp.next
        self.size = self.size - 1
        return dtemp.value

    def remove(self, pos: int) -> Any:
        if self.size == 0:
            return
        remnode = self.node(pos)
        if remnode.next == self.tail:
            self.tail = remnode
        remnode.next = remnode.next.next
        self.size = self.size - 1

    def remove_last(self) -> Any:
        dtemp = self.tail
        del self.tail
        self.tail = None
        self.size = self.size - 1

        if self.size == 0:
            self.data = None
            self.tail = None

        d = self.data
        for x in range(0, self.size-1):
            d = d.next
            if x == self.size-2:
                d.next = None
                self.tail = d

        return dtemp.value

    def append(self, value: Any) -> None:
        append_node = Node(value)
        if self.data is None:
            self.data = append_node
            self.tail = append_node
            self.size = self.size + 1
            return
        self.tail.next = append_node
        self.tail = append_node
        self.size = self.size + 1

    def insert(self, value: Any, pos: int) -> None:
        insert_node = Node(value)
        d = self.data
        for x in range(0, pos):
            d = d.next

        dtemp = d.next
        d.next = insert_node
        insert_node.next = dtemp

        self.size = self.size + 1
