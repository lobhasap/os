echo "Enter the main string:"
read main_string

echo "Enter the substring to search for:"
read substring

main_length=0
sub_length=0
occurrences=0
positions=()

while [ "${main_string:$main_length:1}" != "" ]; do
  main_length=$((main_length + 1))
done

while [ "${substring:$sub_length:1}" != "" ]; do
  sub_length=$((sub_length + 1))
done

for ((i = 0; i <= main_length - sub_length; i++)); do
  match=true
  for ((j = 0; j < sub_length; j++)); do
    if [ "${main_string:$((i + j)):1}" != "${substring:$j:1}" ]; then
      match=false
      break
    fi
  done

  if [ "$match" = true ]; then
    occurrences=$((occurrences + 1))
    positions+=($((i + 1))) # Record position (1-based index)
  fi
done

if [ "$occurrences" -gt 0 ]; then
  echo "Substring found $occurrences time(s)."
  echo "Positions: ${positions[@]}"
else
  echo "Substring not found."
fi