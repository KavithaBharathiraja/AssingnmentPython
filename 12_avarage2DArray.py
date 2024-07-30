 # 12. Write a python  program to find the average score of two students in three papers. NOTE: Given, score of first student is 60, 55 and 70 while score of the second student is 80, 60 and 41. i.e. int[][] score = { {60, 55, 70}, {80, 60, 41} };
scores = [
    [60, 55, 70],
    [80, 60, 41]
]

averages = []

for Student_source in scores:
    sum_source = sum(Student_source)
    average = sum_source/ len(Student_source)
    averages.append(average)

for i, average in enumerate(averages):
    print(f"Average score of student {i + 1}: {average:.2f}")

# Print the average scores using indexing
# student_number = 1
# for average in averages:
#     print(f"Average score of student {student_number}: {average:.2f}")
#     student_number += 1