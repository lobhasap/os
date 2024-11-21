echo "Enter main string: "
read mainstr

echo "Enter sub string: "
read substr

subcount=0
count=0
j=0
pos=()

sublen=${#substr}
mainlen=${#mainstr}

for ((i = 0; i < mainlen; i++)); do
    if [ ${subcount} -eq ${sublen} ]; then
        count=$((count + 1))
        subcount=0  # Reset subcount after a complete match
        i=$((i - 1))  # Recheck this index to ensure proper counting
    elif [ "${mainstr:i:1}" != "${substr:subcount:1}" ]; then
        subcount=0
    elif [ "${mainstr:i:1}" == "${substr:subcount:1}" ]; then
        subcount=$((subcount + 1))
        if [ ${subcount} -eq ${sublen} ]; then
            pos[j]=$((i - subcount + 1))  # Save starting position of match
            j=$((j + 1))
        fi
    fi
done

# Check if the last match completed
if [ ${subcount} -eq ${sublen} ]; then
    count=$((count + 1))
fi

echo "Number of occurrences: ${count}"
echo "Positions: ${pos[*]}"