import threading
import time
import random
from datetime import datetime

# Shared buffer
buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)  # initially has buffer_size empty slots
full = threading.Semaphore(0)  # initially buffer is empty
mutex = threading.Lock()  # mutex for critical section, initial value is unlocked

# Item limit for production/consumption
item_limit = 20
produced_count = 0
consumed_count = 0

# Producer function
def producer():
    global buffer, produced_count
    while produced_count < item_limit:
        item = random.randint(1, 10)  # Produce a random item
        timestamp = datetime.now().strftime("%H:%M:%S")
        empty.acquire()  # Wait for an empty slot
        mutex.acquire()  # Enter critical section
        buffer.append(item)  # Add the item to the buffer
        produced_count += 1
        print(f"[{timestamp}] Produced: {item} at position {len(buffer)}")
        print(f"Buffer after producing: {buffer}")
        mutex.release()  # Leave critical section
        full.release()  # Signal that an item is available
        time.sleep(random.uniform(0.1, 0.5))  # Simulating production time

# Consumer function
def consumer():
    global buffer, consumed_count
    while consumed_count < item_limit:
        full.acquire()  # Wait for an available item
        timestamp = datetime.now().strftime("%H:%M:%S")
        mutex.acquire()  # Enter critical section
        if buffer:  # Check if the buffer is not empty
            item = buffer.pop(0)  # Remove the first item from the buffer
            consumed_count += 1
            print(f"[{timestamp}] Consumed: {item} from position 1")
            print(f"Buffer after consuming: {buffer}")
        mutex.release()  # Leave critical section
        empty.release()  # Signal that a slot is empty
        time.sleep(random.uniform(0.1, 0.5))  # Simulating consumption time

producer_thread1 = threading.Thread(target=producer)
producer_thread2 = threading.Thread(target=producer)
consumer_thread1 = threading.Thread(target=consumer)
consumer_thread2 = threading.Thread(target=consumer)
 
producer_thread1.start()
producer_thread2.start()
consumer_thread1.start()
consumer_thread2.start()

producer_thread1.join()
producer_thread2.join()
consumer_thread1.join()
consumer_thread2.join()
 

# Final message
print("All items have been produced and consumed.")
