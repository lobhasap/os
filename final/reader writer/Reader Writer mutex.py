import threading
import time
import random

# Shared buffer (can be a list of items for simplicity)
buffer = []

# Locks (Mutex)
resource_lock = threading.Lock()
read_count_lock = threading.Lock()
read_count = 0

# Control the number of items produced
max_items = 10  # Max number of items to be produced
items_written = 0  # Counter to track items written


def writer(writer_id):
    global items_written
    while items_written < max_items:
        resource_lock.acquire()

        # Writing (add random item to the buffer)
        item = random.randint(1, 100)  # Random number between 1 and 100
        buffer.append(item)
        items_written += 1
        print(f"Writer {writer_id} is writing {item}.")
        print(f"Buffer after writing: {buffer}")
        time.sleep(1)
        print(f"Writer {writer_id} finished writing at {time.strftime('%H:%M:%S')}")

        resource_lock.release()


def reader(reader_id):
    global read_count
    read_count_lock.acquire()
    read_count += 1
    if read_count == 1:
        resource_lock.acquire()  # First reader locks the resource
    read_count_lock.release()

    # Reading
    print(f"Reader {reader_id} is reading.")
    print(f"Buffer contents: {buffer}")
    time.sleep(1)
    print(f"Reader {reader_id} finished reading at {time.strftime('%H:%M:%S')}")

    read_count_lock.acquire()
    read_count -= 1
    if read_count == 0:
        resource_lock.release()  # Last reader unlocks the resource
    read_count_lock.release()

# Create threads

writers = [threading.Thread(target=writer, args=(i+1,)) for i in range(2)]
readers = [threading.Thread(target=reader, args=(i+1,)) for i in range(3)]

# Start threads
for t in writers + readers:
    t.start()

# Wait for threads to finish
for t in writers + readers:
    t.join()

print("All operations completed.")
