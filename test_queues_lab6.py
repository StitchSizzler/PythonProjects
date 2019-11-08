"""
This program compares the runtime efficiency
for a Bounded Queue and for a Circular Queue
"""

from BoundedQueue import BoundedQueue
from CircularQueue import CircularQueue
import time

def main():
    # create bounded and circular queues
    bounded = BoundedQueue(1000000001)
    circular = CircularQueue(1000000001)
    # add items to both queues
    for i in range(5000000):
        bounded.enqueue(i)
        circular.enqueue(i)
        
    # dequeue Bounded and analyse time
    n = 990
    totalTimeBounded = 0.0
    for i in range(10):
        start = time.time()
        for i in range(500):
            bounded.dequeue()
        end = time.time()
        print("Bounded queue required %10.7f seconds"%(end-start))
        totalTimeBounded=totalTimeBounded+end-start
    print("the average time for Bounded queue was %10.7f for n=%d"%(totalTimeBounded/10,n))
    
    # dequeue Circular and analyse time
    n = 990
    totalTimeCircular = 0.0
    for i in range(10):
        start = time.time()
        for i in range(50000):
            circular.dequeue()
        end = time.time()
        print("Circular queue required %10.7f seconds"%(end-start))
        totalTimeCircular=totalTimeCircular+end-start
    print("the average time for Circular queue was %10.7f for n=%d"%(totalTimeCircular/10,n))            
    
main()