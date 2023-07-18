# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import Queue

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, value):
        # Get the current size of the queue
        size = self.queue.qsize()

        # Enqueue the new element
        self.queue.put(value)

        # Rotate the queue to make the newly added element at the front
        for _ in range(size):
            self.queue.put(self.queue.get())

    def pop(self):
        # Check if the stack is empty
        if self.queue.empty():
            return None

        # Remove and return the top element from the queue
        return self.queue.get()


# Example usage
stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None
