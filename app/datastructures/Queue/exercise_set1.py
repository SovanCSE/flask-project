import threading
import time
from collections import deque

class Queue():

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.appendleft(item)
        print("order added into queue", item)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
         print(len(self.buffer) == 0)

    def get_size(self):
        print(len(self.buffer))

class FoodOrderingSystem:

    def order_placing(self):
        for order in ['pizza','samosa','pasta','biryani','burger']:
            time.sleep(.5)
            queue.enqueue(order)


    def serve_order(self):
        while len(queue.buffer):
            print("Order served out of queue:", queue.dequeue())
            time.sleep(2)

if __name__ == "__main__":
    """
     Designing food system of place order and serve order first come first serve basic using queue 
     process
    """
    foodservedesign = FoodOrderingSystem()
    queue = Queue()
    order_placeing_thread= threading.Thread(target=foodservedesign.order_placing)
    serve_order_thread = threading.Thread(target=foodservedesign.serve_order)


    order_placeing_thread.start()
    time.sleep(1)
    serve_order_thread.start()

    order_placeing_thread.join()
    serve_order_thread.join()

    print("Order Service gets competed and order list =", queue.buffer)