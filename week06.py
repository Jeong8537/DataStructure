class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        self._size = self._size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is Empty!")
        self._size = self._size - 1
        temp = self.front
        self.front = self.front.link
        if self.front is None:
            self.rear = None
        temp.link = None # !
        return temp.data

Q = Queue()

Q.enqueue("자료구조")
Q.enqueue("데이터베이스")
print(Q._size, Q.front.data, Q.rear.data)

Q.dequeue()
Q.dequeue()
print(Q._size, Q.front, Q.rear)