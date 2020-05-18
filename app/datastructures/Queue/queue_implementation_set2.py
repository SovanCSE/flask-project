"""
QUEUE implementation using deque in collections module
"""

from collections import deque

class Queue():

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.appendleft(item)
        print("Added item:", item)

    def dequeue(self):
        print(self.buffer.pop())

    def isEmpty(self):
         print(len(self.buffer) == 0)

    def get_size(self):
        print(len(self.buffer))

    def front(self):
        if len(self.buffer):
            print("", self.buffer[-1])
        else:
            print("Queue is empty")

if __name__ == "__main__":
   queue = Queue()
   queue.enqueue(12)
   queue.enqueue(15)
   queue.enqueue(20)
   queue.dequeue()
   queue.dequeue()
   queue.dequeue()
   print(queue.buffer)
   queue.get_size()
   queue.isEmpty()
