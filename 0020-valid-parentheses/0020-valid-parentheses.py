from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if self.is_empty():
            return None
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

class Solution(object):
    def isValid(self, s):
        stack=Stack()
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in "({[":
                stack.push(i)
            else:
                if stack.is_empty():
                    return False
                if stack.peek()!=pairs[i]:
                    return False
                else:
                    stack.pop()
        return stack.is_empty()

        