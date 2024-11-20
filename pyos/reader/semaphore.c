#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <semaphore.h>

// Global variables to hold the time values
int seconds = 55, minutes = 59, hours = 23;
int update_count = 0; // Counter for updates
const int max_updates = 10; // Maximum number of updates before terminating

// Semaphores for synchronization
sem_t resource_access;    // Controls access to the timer
sem_t reader_count_access; // Synchronizes access to the reader count
int reader_count = 0;      // Number of active readers

// Function to update the time (seconds, minutes, hours)
void* update(void* arg) {
    while (true) {
        // Writers need exclusive access, so they wait for the resource semaphore
        sem_wait(&resource_access);

        // Update time values
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

        // Display updated time for the writer
        printf("Writer %d: Writing clock %02d:%02d:%02d\n", *(int*)arg, hours, minutes, seconds);
        
        // Increment the update count
        update_count++;

        // Release the resource semaphore
        sem_post(&resource_access);

        // Sleep for one second before updating again
        sleep(1);

        // Terminate if max updates reached
        if (update_count >= max_updates) {
            break;
        }
    }
    return NULL;
}

// Function to display the time (read-only)
void* display(void* arg) {
    while (true) {
        // Readers need to synchronize access to the reader count
        sem_wait(&reader_count_access);
        reader_count++;
        if (reader_count == 1) {
            // First reader locks the resource for shared access
            sem_wait(&resource_access);
        }
        sem_post(&reader_count_access);

        // Display the current time
        printf("Reader %d: Reading clock %02d:%02d:%02d\n", *(int*)arg, hours, minutes, seconds);

        // Readers synchronize access to the reader count
        sem_wait(&reader_count_access);
        reader_count--;
        if (reader_count == 0) {
            // Last reader unlocks the resource
            sem_post(&resource_access);
        }
        sem_post(&reader_count_access);

        // Sleep for one second before displaying again
        sleep(1);

        // Terminate if max updates reached
        if (update_count >= max_updates) {
            break;
        }
    }
    return NULL;
}

int main() {
    // Initialize the semaphores
    sem_init(&resource_access, 0, 1);        // Binary semaphore (like a mutex)
    sem_init(&reader_count_access, 0, 1);   // Binary semaphore to protect reader count

    // Set the initial time
    printf("Set the clock to initially 23hrs 59mins 55secs\n");

    // Create the threads for update and display
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

    // Join the threads (wait for them to finish)
    for (int i = 0; i < 2; i++) {
        pthread_join(update_threads[i], NULL);
    }
    for (int i = 0; i < 3; i++) {
        pthread_join(display_threads[i], NULL);
    }

    // Destroy the semaphores before exiting
    sem_destroy(&resource_access);
    sem_destroy(&reader_count_access);

    return 0;
}
