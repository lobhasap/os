#!/bin/bash

# Read array elements
echo "Enter the number of elements:"
read n
echo "Enter the elements:"
for (( i=0; i<n; i++ )); do
    read arr[$i]
done

# Selection Sort
for (( i=0; i<n-1; i++ )); do
    min_idx=$i
    for (( j=i+1; j<n; j++ )); do
        if (( arr[j] < arr[min_idx] )); then
            min_idx=$j
        fi
    done
    # Swap arr[i] and arr[min_idx]
    temp=${arr[$i]}
    arr[$i]=${arr[$min_idx]}
    arr[$min_idx]=$temp
done

# Display sorted array
echo "Sorted array:"
for (( i=0; i<n; i++ )); do
    echo -n "${arr[$i]} "
done
echo
