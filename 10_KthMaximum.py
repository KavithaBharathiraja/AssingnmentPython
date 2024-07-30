# 10. Write a Java program to find the k largest elements in a given array of length n. Elements in the array can be in any order.Here, "k" is number of result you want to check, and "n" is length of an array.
# Example: if k=3, then it will find first three largest number from array.

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k=3

sortedarray = sorted(array, reverse= True)

k_largest = sortedarray[:k]

print(k_largest)