#include <stdio.h> 
 
int findOptimal(int pages[], int n, int frames[], int m, int currIndex) { 
    int farthest = -1, indexToReplace = -1; 
    for (int i = 0; i < m; i++) { 
        int found = 0; 
        for (int j = currIndex + 1; j < n; j++) { 
            if (frames[i] == pages[j]) { 
                found = 1; 
                if (j > farthest) { 
                    farthest = j; 
                    indexToReplace = i; 
                } 
                break; 
            } 
        } 
        if (found == 0) { 
            return i; 
        } 
    } 
    return indexToReplace; 
} 
 
int main() { 
    int pages[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3}; 
    int n = sizeof(pages) / sizeof(pages[0]); 
    int frames[3];  // Number of frames 
    int m = sizeof(frames) / sizeof(frames[0]); 
    int pageFaults = 0; 
 
    // Initialize frames to -1 (empty) 
    for (int i = 0; i < m; i++) { 
        frames[i] = -1; 
    } 
 
    // Traverse through the pages 
    for (int i = 0; i < n; i++) { 
        int page = pages[i]; 
        int found = 0; 
 
        // Check if page is already in frames 
        for (int j = 0; j < m; j++) { 
            if (frames[j] == page) { 
                found = 1; 
                break; 
            } 
        } 
 
        // If page is not found in frames, page fault occurs 
        if (!found) { 
            pageFaults++; 
 
            // Find the optimal page to replace 
            int replaceIndex = findOptimal(pages, n, frames, m, i); 
            frames[replaceIndex] = page; 
        } 
 
        // Display current frame status 
        printf("Frame status after page %d: ", page); 
        for (int j = 0; j < m; j++) { 
            printf("%d ", frames[j]); 
        } 
        printf("\n"); 
    } 
 
    printf("Total page faults: %d\n", pageFaults); 
    return 0; 
} 