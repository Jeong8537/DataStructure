import random


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

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"\nfind! target: {target}"
            else:
                current= current.link
        return f"\nNone Data"

    def remove(self, target):
        if self.head == target:
            self.head.data = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
                print(f"remove! target: {target}")
            previous = current
            current = current.link

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            # print(node.data)
            out_texts = out_texts + str(node.data) + " => "
            node = node.link
        return f"{out_texts}end"


ll = LinkedList()

# for i in range(20):
#     ll.append(random.randint(1, 30))

ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(10))
print(ll.search(8))
print("\n")
ll.remove(-9)
print(ll)

