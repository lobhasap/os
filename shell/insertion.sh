#!/bin/bash
# Function to perform insertion sort
insertion_sort() {
    arr=("$@")
    n=${#arr[@]}
    for ((i = 1; i < n; i++)); do
        key=${arr[i]}
        j=$((i - 1))
        while ((j >= 0 && arr[j] > key)); do
            arr[j + 1]=${arr[j]}
            j=$((j - 1))
        done
        arr[j + 1]=$key
    done
    echo "${arr[@]}"
}

# Main part
echo "Enter the number of elements to be sorted:"
read n
echo "Enter the numbers:"
for ((i = 0; i < n; i++)); do
    read arr[$i]
done

# Call the insertion_sort function and display the sorted result
sorted_arr=($(insertion_sort "${arr[@]}"))
echo "Sorted list:"
echo "${sorted_arr[@]}"
