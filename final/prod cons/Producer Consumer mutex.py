import threading
import time
import random
from datetime import datetime

# Shared buffer
buffer = []
buffer_size = 5
mutex = threading.Lock()  # Unlocked originally (value 1)

# Control variables
max_items = 20  # Total items to produce and consume
total_items_produced = 0
total_items_consumed = 0

# Producer function
def producer():
    global buffer, total_items_produced
    while total_items_produced < max_items:
        item = random.randint(1, 10)
        timestamp = datetime.now().strftime("%H:%M:%S")
        mutex.acquire()
        if len(buffer) < buffer_size:
            buffer.append(item)
            total_items_produced += 1
            print(f"Produced: {item} at position {len(buffer)} at {timestamp}")
        else:
            print(f"Buffer full! Producer is waiting. Current buffer: {buffer}")
        print(f"Current buffer: {buffer}")
        mutex.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulating production time

# Consumer function
def consumer():
    global buffer, total_items_consumed
    while total_items_consumed < max_items:
        timestamp = datetime.now().strftime("%H:%M:%S")
        mutex.acquire()
        if buffer:
            item = buffer.pop(0)
            total_items_consumed += 1
            print(f"Consumed: {item} from position 1 at {timestamp}")
        else:
            print(f"Buffer empty! Consumer is waiting. Current buffer: {buffer}")
        print(f"Current buffer: {buffer}")
        mutex.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulating consumption time

# Threads
producer_thread1 = threading.Thread(target=producer)
producer_thread2 = threading.Thread(target=producer)
consumer_thread1 = threading.Thread(target=consumer)
consumer_thread2 = threading.Thread(target=consumer)
   
# Start threads
producer_thread1.start()
producer_thread2.start()
consumer_thread1.start()
consumer_thread2.start()

# Wait for threads to finish
producer_thread1.join()
producer_thread2.join()
consumer_thread1.join()
consumer_thread2.join()

print("Production and consumption completed.")
