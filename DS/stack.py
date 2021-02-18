class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def get_stack(self):
        return self.stack


# my_stack = Stack()
# print('Is empty', my_stack.is_empty())
# my_stack.push(1)
# my_stack.push('A')
# print('Is empty', my_stack.is_empty())
# print('All Stack', my_stack.get_stack())
# print('Peek is', my_stack.peek())
