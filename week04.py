class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: # LinkedList Empty =>
            self.head = Node(data) # new node (head linked)
            return
        current = self.head
        while current.link:
            current = current.link # next Node
        current.link = Node(data)

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)