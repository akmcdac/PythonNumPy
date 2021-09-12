class Node:
    value: str
    prev: 'Node' = None
    next: 'Node' = None


class SimpleQueue:
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None

    def append(self, value: str):
        new_node = Node()
        new_node.value = value
        if not self._head:
            new_node.next = self._head
            self._head.value = new_node.value
        else:
            pointer = self._head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node.next
            pointer.value = new_node.value

    def appendleft(self, value: str):
        new_node = Node()
        new_node.value = value
        if self._head:
            new_node.prev = self._head
            self._head.next = new_node
        else:
            self._tail = new_node
        self._head = new_node

    def pop(self) -> str:
        try:
            value = self._tail.value
            self._tail = self._tail.next
            try:
                self._tail.prev = None
            except:
                self._head = None
            return value
        except:
            return None

    def popleft(self) -> str:
        try:
            value = self._head.value
            self._head = self._head.next
            try:
                self._head.prev = None
            except:
                self._tail = None
            return value
        except:
            return None

    def add(self, index: int, value: str):
        new_node = Node()
        new_node.value = value
        node = self._head
        for _ in range(index):
            node = node.prev
        if node:
            if node.prev:
                node.prev.next = new_node
            node.prev = new_node
        if node == self._head:
            self._head = new_node
        if not self._tail:
            self._tail = new_node

    def remove(self, index: int):
        node = self._head
        for _ in range(index):
            node = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self._head:
            self._head = node.prev
        if node == self._tail:
            self._tail = node.next


def main():
    queue = SimpleQueue()
    queue.add(0, 'hej')
    queue.add(1, 'Arlen')
    queue.append('akm')
    print(queue.pop())
    print(queue.popleft())
    print(queue.popleft())


if __name__ == "__main__":
    main()
