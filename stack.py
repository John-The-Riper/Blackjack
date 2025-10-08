"""
Filename: Stack.py
Author: <McDougal, Owen>
Created: <09/30/2025>
Instructor: Holtslander
"""
class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self,data):
        new_node = self._Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self):
        if self._head is None:
            raise IndexError('Stack is empty')
        popped_node = self._head
        self._head = self._head.get_next()
        self._size -=1
        return popped_node.get_data()

    def peek(self):
        if self._head is None:
            raise IndexError('Stack is empty')
        return self._head.get_data()

    def __len__(self):
        return self._size

    class _Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
        def get_data(self):
            return self.data
        def get_next(self):
            return self.next
