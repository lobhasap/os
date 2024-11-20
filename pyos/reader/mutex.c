#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>

int seconds = 55, minutes = 59, hours = 23;
int update_count = 0; // Counter for updates
const int max_updates = 10; // Maximum number of updates before terminating

pthread_rwlock_t timer_lock;

void* update(void* arg) {
    while (true) {
        pthread_rwlock_wrlock(&timer_lock);
        seconds++;
        if (seconds == 60) {
            seconds = 0;
            minutes++;
        }
        if (minutes == 60) {
            minutes = 0;
            hours++;
        }
        if (hours == 24) {
            hours = 0;
        }
        printf("Writer %d: Writing clock %02d:%02d:%02d\n", *(int*)arg, hours, minutes, seconds);
        
        update_count++;

        pthread_rwlock_unlock(&timer_lock);

        sleep(1);

        if (update_count >= max_updates) {
            break;
        }
    }
    return NULL;
}

void* display(void* arg) {
    while (true) {
        pthread_rwlock_rdlock(&timer_lock);

        printf("Reader %d: Reading clock %02d:%02d:%02d\n", *(int*)arg, hours, minutes, seconds);
        printf("Reader %d exiting critical section\n", *(int*)arg);

        pthread_rwlock_unlock(&timer_lock);
        sleep(1);
        if (update_count >= max_updates) {
            break;
        }
    }
    return NULL;
}

int main() {
    if (pthread_rwlock_init(&timer_lock, NULL) != 0) {
        printf("Read-Write lock initialization failed\n");
        return 1;
    }

    printf("Set the clock to initially 23hrs 59mins 55secs\n");

    pthread_t update_threads[2], display_threads[3];
    int writer_ids[2] = {1, 2};
    int reader_ids[3] = {1, 2, 3};

    for (int i = 0; i < 2; i++) {
        if (pthread_create(&update_threads[i], NULL, update, &writer_ids[i]) != 0) {
            printf("Error creating update thread %d\n", i + 1);
            return 1;
        }
    }

    for (int i = 0; i < 3; i++) {
        if (pthread_create(&display_threads[i], NULL, display, &reader_ids[i]) != 0) {
            printf("Error creating display thread %d\n", i + 1);
            return 1;
        }
    }

    for (int i = 0; i < 2; i++) {
        pthread_join(update_threads[i], NULL);
    }
    for (int i = 0; i < 3; i++) {
        pthread_join(display_threads[i], NULL);
    }
    pthread_rwlock_destroy(&timer_lock);

    return 0;
}