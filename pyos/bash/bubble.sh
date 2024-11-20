bubble_sort() {
    local arr=("$@")
    local n=${#arr[@]}

    for ((i = 0; i < n-1; i++)); do
        for ((j = 0; j < n-i-1; j++)); do
            if ((arr[j] > arr[j+1])); then
                temp=${arr[j]}
                arr[j]=${arr[j+1]}
                arr[j+1]=$temp
            fi
        done
    done

    echo "${arr[@]}"
}

echo "Enter the number of elements:"
read n

echo "Enter the elements separated by spaces:"
read -a arr

echo "Original array: ${arr[@]}"

sorted_arr=$(bubble_sort "${arr[@]}")

echo "Sorted array: $sorted_arr"