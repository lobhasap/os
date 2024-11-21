def find_optimal_page(pages, frames, total_frames, current_index, total_pages):
    index = -1
    farthest = -1

    # Check each frame
    for i in range(total_frames):
        if frames[i] == -1:
            return i  # Empty frame found

        j = current_index + 1
        # Look ahead in the page sequence
        while j < total_pages:
            if frames[i] == pages[j]:
                if j > farthest:
                    farthest = j
                    index = i
                break
            j += 1

        # If the page is never used again
        if j == total_pages:
            return i

    # If no future references, use the first frame
    return index if index != -1 else 0


def optimal_page_replacement():
    # Accept input
    total_pages = int(input("Enter the total number of pages: "))
    pages = list(map(int, input("Enter the page reference sequence: ").split()))
    total_frames = int(input("Enter the total number of frames: "))
    display_frames = int(input(f"Enter the number of frames to display in output (up to {total_frames}): "))
    display_frames = min(display_frames, total_frames)

    frames = [-1] * total_frames
    page_hits = 0
    page_faults = 0
    next_frame_index = 0  # To keep track of the next available frame

    # Optimal Page Replacement Algorithm
    for i in range(total_pages):
        is_page_present = False

        # Check if the page is already in frames
        for j in range(total_frames):
            if frames[j] == pages[i]:
                is_page_present = True
                page_hits += 1
                break

        # If page is not present
        if not is_page_present:
            page_faults += 1

            # If there are empty frames available
            if next_frame_index < total_frames:
                frames[next_frame_index] = pages[i]
                next_frame_index += 1
            else:
                # Find the optimal page to replace
                optimal_index = find_optimal_page(pages, frames, total_frames, i, total_pages)
                frames[optimal_index] = pages[i]

        # Display the current state of frames
        print(f"\nFrame State after accessing page {pages[i]}:")
        for j in range(display_frames):
            if frames[j] != -1:
                print(f"| {frames[j]:3d} ", end="")
            else:
                print("|      ", end="")
        print("|")

    # Calculate and display page hit ratio and page fault ratio
    hit_ratio = page_hits / total_pages
    fault_ratio = page_faults / total_pages

    print(f"\n\nTotal Page Hits: {page_hits}")
    print(f"Total Page Faults: {page_faults}")
    print(f"Page Hit Ratio: {hit_ratio:.2f}")
    print(f"Page Fault Ratio: {fault_ratio:.2f}")


# Run the program
optimal_page_replacement()
