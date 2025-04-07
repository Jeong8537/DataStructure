class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def all_peek(self):
        return self.items[:]

s1 = Stack()
s2 = Stack()
# print(s1.is_empty())

s1.push("DataStruct")
print(s1.is_empty())
print(s2.is_empty())

s1.push("DataBase")
print(s1.size())
# print(s2.size())

print(s1.peek())
print(s1.all_peek())

print(s1.pop())