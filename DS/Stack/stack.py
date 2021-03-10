class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def get_stack(self):
        return self.stack

    def size(self):
        return len(self.stack)

    def __len__(self):
        return self.size()

    def __str__(self):
        s = ""
        for i in range(len(self.stack)):
            if type(self.stack[i]) is not int:
                s += str(self.stack[i].data) + "-"
            else:
                s += str(self.stack[i]) + "-"
        return s


# my_stack = Stack()
# print('Is empty', my_stack.is_empty())
# my_stack.push(1)
# my_stack.push('A')
# print('Is empty', my_stack.is_empty())
# print('All Stack', my_stack.get_stack())
# print('Peek is', my_stack.peek())
