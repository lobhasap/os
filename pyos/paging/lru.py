def findLRU(time, n):
    min_time = time[0]
    pos = 0
    for i in range(1, n):
        if time[i] < min_time:
            min_time = time[i]
            pos = i
    return pos


def main():
    num_frames = int(input("Enter number of frames: "))
    num_pages = int(input("Enter number of pages: "))
    
    print("Enter page reference string: ")
    pages = [int(input()) for _ in range(num_pages)]

    frames = [-1] * num_frames  # Initialize frames as empty
    time = [0] * num_frames  # Track the time each frame was last used
    page_faults = 0
    counter = 0

    for i in range(num_pages):
        found = False

        for j in range(num_frames):
            if frames[j] == pages[i]:
                found = True
                counter += 1
                time[j] = counter  # Update the last accessed time
                break

        if not found:  # Page fault occurs
            if -1 in frames:  # If there's an empty frame
                empty_index = frames.index(-1)
                frames[empty_index] = pages[i]
                counter += 1
                time[empty_index] = counter
            else:
                pos = findLRU(time, num_frames)
                frames[pos] = pages[i]
                counter += 1
                time[pos] = counter
            page_faults += 1

        print("\nFrames: ", end="")
        for frame in frames:
            print(frame, end=" ")

    print(f"\nTotal Page Faults = {page_faults}")


if __name__ == "__main__":
    main()