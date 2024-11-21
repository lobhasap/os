#!/bin/bash
is_palindrome() {
    local str
    echo "Enter a string to check if it's a palindrome:"
    read str  # Read the string inside the function

    local len=${#str}  # Calculate the length of the string
    local reversed_str=""

    # Reverse the string manually
    for (( i=len-1; i>=0; i-- )); do
        reversed_str="${reversed_str}${str:$i:1}"
    done

    # Check if the original string is equal to the reversed string
    if [ "$str" = "$reversed_str" ]; then
        echo "The string is a palindrome."
    else
        echo "The string is not a palindrome."
    fi
}

# Call the palindrome-checking function
is_palindrome
