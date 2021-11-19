student_marks = [23, 45, 89, 90, 56, 91] 
length = len(student_marks)
i = 0
total_marks = 0
while i < len(student_marks):
    total_marks = student_marks[i] + total_marks
    i = i + 1
print ("Total Marks: " + str(total_marks))