def findOptimal(pages, n, frames, m, curr_index):
    farthest = -1
    index_to_replace = -1

    for i in range(m):
        found = False
        for j in range(curr_index + 1, n):
            if frames[i] == pages[j]:
                found = True
                if j > farthest:
                    farthest = j
                    index_to_replace = i
                break
        if not found:
            return i  # No future use of this frame, replace it

    return index_to_replace


def main():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    n = len(pages)

    frames = [-1] * 3
    m = len(frames)

    page_faults = 0

    for i in range(n):
        page = pages[i]
        found = False

        for j in range(m):
            if frames[j] == page:
                found = True
                break

        if not found:
            page_faults += 1
            replace_index = findOptimal(pages, n, frames, m, i)
            frames[replace_index] = page

        print(f"Frame status after page {page}: {frames}")

    print(f"Total page faults: {page_faults}")


if __name__ == "__main__":
    main()