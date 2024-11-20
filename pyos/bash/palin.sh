pali(){
    echo "Enter a String"
    read str

    n=${#str}
    rev=""

    for ((i=n-1;i>=0;i--)); do
    rev="${rev}${str:i:1}"
    done

    if [[ "${str}" == "${rev}" ]]; then
    echo "The string is a palindrome"
    else
    echo "The string is not a palindrome"
    fi
}

pali