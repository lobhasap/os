import threading
import random
import time

BUFFER_SIZE = 3
MAX_ITEMS = 10

buffer = [0] * BUFFER_SIZE
in_index = 0
out_index = 0
count = 0
item_produced = 0
item_consumed = 0

mutex = threading.Lock()
not_full = threading.Condition(mutex)
not_empty = threading.Condition(mutex)

def producer(producer_id):
    global buffer, in_index, count, item_produced

    while True:
        item = random.randint(0, 99)

        with mutex:
            if item_produced >= MAX_ITEMS:
                break

            while count == BUFFER_SIZE:
                print(f"Producer {producer_id} Blocked.....Buffer Full")
                not_full.wait()

            buffer[in_index] = item
            print(f"Producer {producer_id} inserting {item} in slot {in_index + 1}")
            in_index = (in_index + 1) % BUFFER_SIZE
            count += 1
            item_produced += 1

            not_empty.notify()

        time.sleep(1)

def consumer(consumer_id):
    global buffer, out_index, count, item_consumed

    while True:
        with mutex:
            if item_consumed >= MAX_ITEMS:
                break

            while count == 0:
                print(f"Consumer {consumer_id} blocked ...... buffer empty")
                not_empty.wait()

            item = buffer[out_index]
            print(f"Consumer {consumer_id} consuming {item} from slot {out_index + 1}")
            item_consumed += 1
            count -= 1
            out_index = (out_index + 1) % BUFFER_SIZE

            not_full.notify()

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
