# 1.  Write a python program to print an array after interchanging the rows and columns of a given two-dimensional array.Original Array:10 20 3040 50 60 After changing the rows and columns of the said array:10 4020 5030 60

original_array = [
    [10, 20, 30],
    [40, 50, 60]
]

row_count = len(original_array)
col_count = len(original_array[0])

transported_array = [[0] * row_count for _ in  range(col_count)]

for i in range(row_count):
    for j in range(col_count):
        transported_array[j][i] = original_array[i][j]

print("original_array")
for row in original_array:
    print(row)

print("\ntransported_array")
for row in transported_array:
    print(row)