def main():
    pages = []
    frames = []
    count = []  # To track how recently each frame was used
    page_faults = 0
    page_hits = 0
    next_frame_index = 0

    # Accept the sequence of pages and frame size
    total_pages = int(input("Enter the total number of pages: "))
    print("Enter the page reference sequence: ")
    pages = [int(input()) for _ in range(total_pages)]

    total_frames = int(input("Enter the total number of frames: "))
    display_frames = int(input(f"Enter the number of frames to display in output (up to {total_frames}): "))
    if display_frames > total_frames:
        display_frames = total_frames

    # Initialize frames and counts
    frames = [-1] * total_frames
    count = [0] * total_frames

    # LRU Page Replacement Algorithm
    for i in range(total_pages):
        is_page_present = False

        # Check if the page is already in frames
        for j in range(total_frames):
            if frames[j] == pages[i]:
                is_page_present = True
                page_hits += 1
                count[j] = 0  # Reset count for the current page

                # Increment counts for all other pages
                for k in range(total_frames):
                    if k != j and frames[k] != -1:
                        count[k] += 1
                break

        # If page is not present
        if not is_page_present:
            page_faults += 1

            # If there are empty frames available
            if next_frame_index < total_frames:
                frames[next_frame_index] = pages[i]
                count[next_frame_index] = 0

                # Increment counts for existing pages
                for k in range(next_frame_index):
                    count[k] += 1

                next_frame_index += 1
            else:
                # Replace the least recently used page
                min_count_index = count.index(max(count))  # Find frame with highest count
                frames[min_count_index] = pages[i]
                count[min_count_index] = 0

                # Increment counts for all other pages
                for k in range(total_frames):
                    if k != min_count_index:
                        count[k] += 1

        # Display the current state of frames with blocks
        print(f"\nFrame State after accessing page {pages[i]}:")
        for j in range(display_frames):
            if frames[j] != -1:
                print(f"| {frames[j]:3d} ", end="")
            else:
                print("|     ", end="")
        print("|")

    # Calculate and display page hit ratio and page fault ratio
    hit_ratio = page_hits / total_pages
    fault_ratio = page_faults / total_pages

    print("\n\nTotal Page Hits:", page_hits)
    print("Total Page Faults:", page_faults)
    print(f"Page Hit Ratio: {hit_ratio:.2f}")
    print(f"Page Fault Ratio: {fault_ratio:.2f}")


if __name__ == "__main__":
    main()
