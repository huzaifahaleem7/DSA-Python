import threading
from collections import deque
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

def place_order(orders, q):
    for order in orders:
        print(f"Placing Order {order}")
        q.enqueue(order)
        time.sleep(0.5)

def server_order(q):
    time.sleep(1)
    while True:
        if q.is_empty():
            break
        order = q.dequeue()
        print(f"Serving Order {order}")
        time.sleep(2)

# if __name__ == "__main__":
#     q = Queue()
#     orders = ['pizza','samosa','pasta','biryani','burger']
    
#     t1 = threading.Thread(target=place_order, args=(orders, q))
#     t2 = threading.Thread(target=server_order, args=(q,))
    
#     t1.start()
#     t2.start()
    
#     t1.join()
#     t2.join()
    
    
#     print("All orders have been placed and served.")
    
    
#     Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.

# Solution
    
def generate_binary_numbers(n):
    q = Queue()
    q.enqueue("1")
    
    for i in range(n):
        front = q.front()
        print(front)
        q.dequeue()
        
        q.enqueue(front + "0")
        q.enqueue(front + "1")

if __name__ == "__main__":
    generate_binary_numbers(10)