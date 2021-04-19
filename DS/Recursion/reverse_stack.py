from Stack.stack import Stack


def insert_at_bottom(my_stack, item):  # Recursive function that inserts an element at the bottom of a stack.
    # Base case
    if my_stack.is_empty():
        my_stack.push(item)

    # Recursive case
    else:
        temp = my_stack.pop()
        insert_at_bottom(my_stack, item)
        my_stack.push(temp)


def reverse_stack(my_stack):
    if not my_stack.is_empty():
        temp = my_stack.pop()
        reverse_stack(my_stack)
        insert_at_bottom(my_stack, temp)


my_stack = Stack()
my_stack.push(8)
my_stack.push(5)
my_stack.push(3)
my_stack.push(2)
print('Original Stack', my_stack.get_stack())
reverse_stack(my_stack)
print("Reversed Stack", my_stack.get_stack())
