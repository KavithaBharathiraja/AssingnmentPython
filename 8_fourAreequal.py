# 8.Write a python program that accepts four integer from the user and prints equal if all four are equal, and not equal otherwise.

a = int(input("Enter a positive number for a: "))
b = int(input("Enter a positive number for b: "))
c = int(input("Enter a positive number for c: "))
d = int(input("Enter a positive number for d: "))

if a==b and b==c and c==d:
    print("four numbers are equal!")
else:
    print("four numbers are not equal!")

