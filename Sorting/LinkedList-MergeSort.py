class LinkedList:
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def __iter__(self):
        class _Iterator:
            def __init__(self, LinkedList):
                self._LinkedList = LinkedList
                self.pointer = self._LinkedList._head

            def __next__(self):
                if self.pointer is None:
                    raise StopIteration
                else:
                    result = self.pointer
                    self.pointer = self.pointer.next
                    return result

        return _Iterator(self)

    def __str__(self):
        result = '['
        pointer = self._head
        while pointer is not None:
            if pointer.next is None:
                result += f'{pointer.data}'
                break
            result += f'{pointer.data}, '
            pointer = pointer.next
        result += ']'

        return result

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._length

    def append(self, data):
        """
        Add an element to the end of the LinkedList.
        :param data:
        """
        if self._length == 0:
            node = self._Node(data)
            self._head = node
            self._tail = node
            self._length += 1

        elif self._length != 0:
            node = self._Node(data)
            self._tail.next = node
            self._tail = node
            self._length += 1

    def prepend(self, data):
        """
        Add an element to the beginning of the LinkedList.
        :param data:
        """
        if self._length == 0:
            node = self._Node(data)
            self._head = node
            self._tail = node
            self._length += 1

        elif self._length != 0:
            node = self._Node(data)
            pointer = self._head
            self._head = node
            node.next = pointer
            self._length += 1

    def search(self, key):
        """
        Search for the first node contaning data that matches the key.
        :param key:
        :return Node or 'None' if not found.:
        """
        pointer = self._head
        while pointer:
            if pointer.data == key:
                return pointer
            else:
                pointer = pointer.next
        return None

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return f'<Node: {self.data}>'


l = LinkedList()
l.append("hello")

print(l)
