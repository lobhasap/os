#!/bin/bash
# Function to perform bubble sort
bubble_sort() {
    n=$1
    num=("${@:2}") # Array of numbers to be sorted
    for ((i = 0; i < n-1; i++)); do
        for ((j = 0; j < n-i-1; j++)); do
            if [ "${num[j]}" -gt "${num[$((j+1))]}" ]; then
                # Swap num[j] and num[j+1]
                temp=${num[j]}
                num[$j]=${num[$((j+1))]}
                num[$((j+1))]=$temp
            fi
        done
    done
    # Return the sorted array
    echo "${num[@]}"
}

# Start
echo "Enter the number of elements to be sorted (max 100):"
read n

# Test Condition: Maximum number of elements allowed is 100
if [ "$n" -gt 100 ]; then
    echo "Error: You can enter a maximum of 100 elements."
    exit 1
fi

# Accept the numbers in an array
echo "Enter the numbers (negative numbers are allowed):"
for ((i = 0; i < n; i++)); do
    read num[$i]
done

# Call the bubble_sort function and store the sorted result
sorted_nums=($(bubble_sort "$n" "${num[@]}"))

# Display the sorted list
echo "Sorted list:"
echo "${sorted_nums[@]}"

# Stop
