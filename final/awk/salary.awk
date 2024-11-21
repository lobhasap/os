#!/usr/bin/awk -f

BEGIN {
    # Print the header of the report
    printf "%-10s %-10s %-10s %-10s %-10s %-10s\n", "Roll No.", "Name", "BS", "DA", "HRA", "GS"
    printf "-------------------------------------------------------------\n"
}

# Process each line of the input file
{
    split($0, fields, ":")       # Split the line into fields based on ":"
    roll_no = fields[1]          # Extract Roll No.
    name = fields[2]             # Extract Name
    bs = fields[3]               # Extract Basic Salary
    da = 0.5 * bs                # Calculate DA
    hra = 0.2 * bs               # Calculate HRA
    gs = bs + da + hra           # Calculate Gross Salary

    # Print the formatted output
    printf "%-10s %-10s %-10.2f %-10.2f %-10.2f %-10.2f\n", roll_no, name, bs, da, hra, gs
}

END {
    print "-------------------------------------------------------------"
}



emp data file 101:John:30000
102:Alice:40000
103:Bob:50000
104:Jane:45000