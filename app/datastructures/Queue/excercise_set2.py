from collections import deque

class Queue():

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.appendleft(item)
        # print("order added into queue", item)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
         print(len(self.buffer) == 0)

    def get_size(self):
        print(len(self.buffer))

    def front(self):
        if len(self.buffer):
            # print("", self.buffer[-1])
            return self.buffer[-1]
        else:
            print("Queue is empty")


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")
    print(numbers_queue.buffer)
    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()

if __name__ == "__main__":
    """
     Produce binary number between 1 to 10 using queue concept
    """
    produce_binary_numbers(10)

