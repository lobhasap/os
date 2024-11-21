#!/usr/bin/awk -f

BEGIN {
    # Define student marks in an associative array
    students["John"] = "85 10 78 89 88"
    students["Doe"] = "45 38 50 62 58"
    students["Alice"] = "76 84 79 91 87"
    students["Bob"] = "39 82 55 70 65"

    # Print the header
    print "Student Marks, Average, and Grades:"

    # Loop through each student
    for (name in students) {
        marks = students[name]
        split(marks, marks_array, " ")
        fail_flag = 0
        total = 0
        count = 0

        # Print the student's marks
        printf "%s: ", name
        for (i in marks_array) {
            printf "%s ", marks_array[i]
        }

        # Process the marks to calculate the total, count, and check for failure
        for (i in marks_array) {
            mark = marks_array[i]
            total += mark
            count++
            if (mark < 40) {
                fail_flag = 1
            }
        }

        # Calculate the average
        average = total / count

        # Determine the grade
        if (fail_flag) {
            grade = "Fail"
        } else if (average >= 90) {
            grade = "A"
        } else if (average >= 75) {
            grade = "B"
        } else if (average >= 60) {
            grade = "C"
        } else if (average >= 50) {
            grade = "D"
        } else {
            grade = "E"
        }

        # Print the average and grade
        printf "-> Average: %.2f -> Grade: %s\n", average, grade
    }
}
