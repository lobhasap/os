def main():
    frames = []
    page_faults = 0
    oldest = 0

    num_frames = int(input("Enter number of frames: "))

    frames = [-1] * num_frames

    num_pages = int(input("Enter number of pages: "))

    print("Enter page reference string: ")
    pages = [int(input()) for _ in range(num_pages)]

    for i in range(num_pages):
        found = False

        for j in range(num_frames):
            if frames[j] == pages[i]:
                found = True
                break

        if not found:  # Page fault occurs
            frames[oldest] = pages[i]
            oldest = (oldest + 1) % num_frames
            page_faults += 1

        print("\nFrames: ", end="")
        for k in frames:
            print(k, end=" ")

    print(f"\nTotal Page Faults = {page_faults}")


if __name__ == "__main__":
    main()