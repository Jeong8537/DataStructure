class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            # raise IndexError('pop from empty stack!')
            return f"Stack is empty! Noting to delete | {self.top}"
        popped_node = self.top
        self.top = self.top.link
        return popped_node.data


s1 = Stack()
print(s1.pop())

s1.push("Data_struct")
print(s1.pop())
print(s1.pop())
