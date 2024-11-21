import threading
import time
import random

# Semaphore and other global variables
resource = threading.Semaphore(1)
rcount_mutex = threading.Semaphore(1)
read_count = 0

# Shared resource: a buffer with 3 elements
buffer = [0] * 3

def get_current_time():
    #"""Returns the current system time in HH:MM:SS format."""
    return time.strftime("%H:%M:%S")

def reader(reader_id):
    global read_count
    while True:
        # Entry section for reader
        rcount_mutex.acquire()
        read_count += 1
        if read_count == 1:
            resource.acquire()  # First reader locks the resource
        rcount_mutex.release()

        # Critical section (reading)
        pos = random.randint(0, 2)  # Random position to read from
        print(f"[{get_current_time()}] Reader {reader_id} is reading {buffer[pos]} from position {pos}")
        time.sleep(1)  # Simulate reading time

        # Exit section for reader
        rcount_mutex.acquire()
        read_count -= 1
        if read_count == 0:
            resource.release()  # Last reader unlocks the resource
        rcount_mutex.release()

        # Simulate time between readings
        time.sleep(2)

def writer(writer_id):
    while True:
        # Entry section for writer
        resource.acquire()  # Writers lock the resource

        # Critical section (writing)
        pos = random.randint(0, 2)  # Random position to write to
        value = random.randint(1, 9)  # Random value to write
        buffer[pos] = value
        print(f"[{get_current_time()}] Writer {writer_id} is writing {value} to position {pos}")
        time.sleep(1)  # Simulate writing time

        # Exit section for writer
        resource.release()  # Writers unlock the resource

        # Simulate time between writings
        time.sleep(3)

if __name__ == "__main__":
    reader_threads = []
    writer_threads = []

    
    # Create writer threads
    for i in range(2):
        writer_thread = threading.Thread(target=writer, args=(i + 1,))
        writer_threads.append(writer_thread)
        writer_thread.start()
        
        # Create reader threads
    for i in range(3):
        reader_thread = threading.Thread(target=reader, args=(i + 1,))
        reader_threads.append(reader_thread)
        reader_thread.start()
