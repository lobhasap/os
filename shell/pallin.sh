#!/bin/bash
# Function to check if a string is a palindrome
is_palindrome() 
{
 str=$1
 len=${#str}
 pointer=0
 flag=true

 while [[ $pointer -lt $((len / 2)) ]]; do
 if [[ ${str:$pointer:1} != ${str:$(($len-$pointer-1)):1} ]]; then
 flag=false
 break
 fi

 pointer=$((pointer + 1))
 done


 # Display result based on flag
 if $flag; then
 echo "String is a palindrome"
 else
 echo "String is not a palindrome"
 fi
 
}



# Start
echo "Enter a string:"
read str
# Test condition: String should not be NULL
if [ -z "$str" ]; then
 echo "String should not be NULL."
 exit 1
fi
# Call the function with the user input
is_palindrome "$str"