#!/bin/bash

# Function to check if substring is present in the string
check_substring() {
    local string="$1"
    local substring="$2"
    local count=0
    local pos=0

    while [[ $string == *"$substring"* ]]; do
        # Find the position of the substring
        pos=$(expr index "$string" "$substring")
        echo "Occurrence found at position: $((pos - 1))"
        count=$((count + 1))
        # Remove the found substring from the string
        string="${string:$pos}"
    done

    if ((count > 0)); then
        echo "Substring '$substring' is present in the string."
        echo "Number of occurrences: $count"
    else
        echo "Substring '$substring' is NOT present in the string."
    fi
}

# Main script execution
read -p "Enter the main string: " main_string
read -p "Enter the substring to check: " sub_string

check_substring "$main_string" "$sub_string"
