import threading
import time
import random

BUFFER_SIZE = 3
MAX_ITEMS = 10

buffer = [0] * BUFFER_SIZE
in_index = 0
out_index = 0
item_produced = 0
item_consumed = 0

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)


def producer(producer_id):
    global buffer, in_index, item_produced

    while True:
        item = random.randint(0, 99)

        empty.acquire()
        mutex.acquire()

        if item_produced >= MAX_ITEMS:
            mutex.release()
            empty.release()
            break

        buffer[in_index] = item
        print(f"Producer {producer_id} inserting {item} in slot {in_index + 1}")
        in_index = (in_index + 1) % BUFFER_SIZE
        item_produced += 1

        mutex.release()
        full.release()

        time.sleep(1)


def consumer(consumer_id):
    global buffer, out_index, item_consumed

    while True:
        full.acquire()
        mutex.acquire()

        if item_consumed >= MAX_ITEMS:
            mutex.release()
            full.release()
            break

        item = buffer[out_index]
        print(f"Consumer {consumer_id} consuming {item} from slot {out_index + 1}")
        out_index = (out_index + 1) % BUFFER_SIZE
        item_consumed += 1

        mutex.release()
        empty.release()


if __name__ == "__main__":
    producer_threads = []
    consumer_threads = []

    for i in range(2):
        producer_thread = threading.Thread(target=producer, args=(i + 1,))
        consumer_thread = threading.Thread(target=consumer, args=(i + 1,))
        producer_threads.append(producer_thread)
        consumer_threads.append(consumer_thread)

    for thread in producer_threads + consumer_threads:
        thread.start()

    for thread in producer_threads + consumer_threads:
        thread.join()

    print("Program completed.")
