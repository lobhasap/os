#!/bin/bash
# Function to perform merge sort
merge_sort() {
    local arr=("$@")
    local n=${#arr[@]}

    # Base case: array with one or no element is already sorted
    if [ "$n" -le 1 ]; then
        echo "${arr[@]}"
        return
    fi

    # Find the midpoint of the array
    mid=$((n / 2))

    # Split the array into two halves
    left=("${arr[@]:0:$mid}")
    right=("${arr[@]:$mid}")

    # Recursively sort both halves
    left_sorted=($(merge_sort "${left[@]}"))
    right_sorted=($(merge_sort "${right[@]}"))

    # Merge the sorted halves
    merge "${left_sorted[@]}" "${right_sorted[@]}"
}

# Helper function to merge two sorted arrays
merge() {
    local left=("$@")
    local right=("${left[@]:${#left[@]}}")
    local result=()

    while [ ${#left[@]} -gt 0 ] && [ ${#right[@]} -gt 0 ]; do
        if [ "${left[0]}" -le "${right[0]}" ]; then
            result+=("${left[0]}")
            left=("${left[@]:1}")
        else
            result+=("${right[0]}")
            right=("${right[@]:1}")
        fi
    done

    # Append any remaining elements from either left or right
    result+=("${left[@]}" "${right[@]}")

    echo "${result[@]}"
}

# Main part
echo "Enter the number of elements to be sorted:"
read n
echo "Enter the numbers:"
for ((i = 0; i < n; i++)); do
    read arr[$i]
done

# Call the merge_sort function and display the sorted result
sorted_arr=($(merge_sort "${arr[@]}"))
echo "Sorted list:"
echo "${sorted_arr[@]}"
