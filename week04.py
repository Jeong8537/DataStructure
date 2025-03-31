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
        while current.link:
            if current.data == target:
                return f"find! target: {target}"
            else:
                current= current.link
        return f"None Data"

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            # print(node.data)
            out_texts = out_texts + str(node.data) + " => "
            node = node.link
        return out_texts + "end"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(11))
print(ll.search((10)))