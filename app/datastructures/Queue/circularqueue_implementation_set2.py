"""
CIRCULAR QUEUE implementation using list in python
Notes:
    Enqueue operation: Enqueue is a operation for adding an element into Queue at REAR end
    Dequeue operation: Dequeue is a operation for removing an element from Queue from FRONT end
    All Queue operations always take as constant time as O(1)
"""

class CircularQueue():
    def __init__(self):
        self.MAX_CAPACITY = 3
        self.queue_list = ['' for i in range(self.MAX_CAPACITY)]
        self.rear = -1 ##(rear end to add element)
        self.front = -1 ##(front end to remove element)

    def isEmpty(self):
        if self.rear == -1 and self.front == -1:
            print("Queue is empty")
            return True

    def isFull(self):
        if (self.rear + 1) % self.MAX_CAPACITY == self.front:
            print("Queue is full")
            return True

    def enqueue(self, item):
        if self.isFull():
            return False
        elif self.isEmpty():
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.MAX_CAPACITY
        self.queue_list[self.rear] = item
        print("added item", self.queue_list[self.rear] )
        # return item

    def dequeue(self):
        if self.isEmpty():
            return False
        elif self.rear == self.front:
            delete_index = self.front
            self.rear = self.front = -1
        else:
            delete_index = self.front
            self.front = (self.front + 1) % self.MAX_CAPACITY

        delete_item = self.queue_list[delete_index]
        self.queue_list[delete_index] = ''
        print("deleted item", delete_item)
        # return delete_item

    def latest_element_to_delete(self):
        if self.isEmpty():
            return
        print("latest element to delete: ", self.queue_list[self.front])
        # return self.queue_list[self.front]

    def latest_inserted_element(self):
        if self.isEmpty():
            return
        print("latest inserted element: ",self.queue_list[self.rear])
        # return self.queue_list[self.rear]

    def display_queue(self):
        print(self.queue_list)


if __name__ == "__main__":
    queue = CircularQueue()

    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(25)
    queue.dequeue()
    queue.dequeue()
    queue.display_queue()
    queue.enqueue(30)
    queue.enqueue(35)
    queue.dequeue()
    queue.display_queue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display_queue()






