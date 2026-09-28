import array

PASS_MARK = 50 

marks = array.array('i', [65, 72, 48, 80, 75])

total = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]

average = total / 5

print("Student marks:", marks)
print("Total:", total)
print("Average:", average)
print("Passed:", average >= PASS_MARK)













