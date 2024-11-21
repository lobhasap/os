#!/bin/bash

bubble_sort() {
    local array=("$@")
    local n=${#array[@]}
    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < n-i-1; j++)); do
            if (( array[j] > array[j+1] )); then
                # Swap elements
                temp=${array[j]}
                array[j]=${array[j+1]}
                array[j+1]=${temp}
            fi
        done
    done
    # Print the sorted array
    echo "Sorted array: ${array[*]}"
}


# Print each element passed to the script
echo "Input elements:"
for element in "$@"; do
    echo "$element"
done

# Call the bubble_sort function with the provided arguments
bubble_sort "$@"
