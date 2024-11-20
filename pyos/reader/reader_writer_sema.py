import threading
import time
import random

clock_data = {
    "hours": 23,
    "minutes": 59,
    "seconds": 55
}

mutex = threading.Semaphore(1)  # Protects read_count variable
write_lock = threading.Semaphore(1)  # Ensures exclusive access for writers

read_count = 0  # Number of active readers
iterations = 5  # Number of iterations per reader/writer


def simulate_delay():
    time.sleep(random.uniform(0.1, 0.5))  # Delay between 0.1s and 0.5s

def increment_clock():
    global clock_data
    clock_data["seconds"] += 1
    if clock_data["seconds"] == 60:
        clock_data["seconds"] = 0
        clock_data["minutes"] += 1
        if clock_data["minutes"] == 60:
            clock_data["minutes"] = 0
            clock_data["hours"] += 1
            if clock_data["hours"] == 24:
                clock_data["hours"] = 0


def reader(reader_id):
    global read_count
    for _ in range(iterations):
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            write_lock.acquire()  # First reader locks writers
        mutex.release()

        print(f"Reader {reader_id} reading clock {clock_data['hours']:02}:{clock_data['minutes']:02}:{clock_data['seconds']:02}")
        simulate_delay()  # Simulate reading time

        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            write_lock.release()  # Last reader unlocks writers
        mutex.release()

        print(f"Reader {reader_id} exiting critical section")
        simulate_delay()  # Simulate delay between read operations


def writer(writer_id):
    for _ in range(iterations):
        write_lock.acquire()  # Writer locks the resource

        increment_clock()
        print(f"Writer {writer_id} writing clock {clock_data['hours']:02}:{clock_data['minutes']:02}:{clock_data['seconds']:02}")
        simulate_delay()  # Simulate writing time

        write_lock.release()  # Unlock the resource
        simulate_delay()  # Simulate delay between write operations


if __name__ == "__main__":
    random.seed(time.time())  # Seed the random number generator

    num_readers = 3
    num_writers = 2

    reader_threads = []
    writer_threads = []

    for i in range(num_readers):
        thread = threading.Thread(target=reader, args=(i + 1,))
        reader_threads.append(thread)

    for i in range(num_writers):
        thread = threading.Thread(target=writer, args=(i + 1,))
        writer_threads.append(thread)

    for thread in reader_threads + writer_threads:
        thread.start()

    for thread in reader_threads + writer_threads:
        thread.join()

    print("All readers and writers have finished.")