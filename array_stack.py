class ArrayStack():
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def push(self, item):
        """Add element item to the top of the stack."""
        self._data.append(item)

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def __str__(self):
        return ''

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]


if __name__ == '__main__':
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print len(S)
    print S.pop()
    print S.is_empty()
    print S.pop()
    print S.is_empty()
    S.push(7)
    S.push(9)
    print S.top()
    S.push(4)
    print len(S)
    print S.pop()
    S.push(6)
