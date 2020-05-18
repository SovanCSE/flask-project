"""
QUEUE implementation using linkedlist
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def get_size(self):
        count = 0
        itr_head = self.head
        while itr_head:
            count+=1
            itr_head = itr_head.next
        return count

    def enqueue(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        print("Item added", node.data)

    def dequeue(self):
        if not self.get_size():
            print("Queue is empty")
        else:
            if self.get_size() == 1:
                print("Item removed", self.head.data)
                self.head = None
            else:
                itr_head = self.head
                while itr_head.next.next:
                    itr_head = itr_head.next
                print("Item removed", itr_head.next.data)
                itr_head.next = None

    def print_queue(self):
        li = []
        itr_head = self.head
        while itr_head:
            li.append(itr_head.data)
            itr_head = itr_head.next
        print("Current Queue elements:", li)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(12)
    queue.enqueue(15)
    queue.enqueue(17)
    queue.enqueue(19)
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print("Size of the queue", queue.get_size())
    queue.print_queue()