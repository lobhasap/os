{
    if (NF > 1) {  # Ensure there's at least a name and one mark
        studentName = $1
        grade = "Pass"

        for (i = 2; i <= NF; i++) {
            if ($i < 40) {
                grade = "Fail"
                break
            }
        }
        
        print studentName, grade
    }
}