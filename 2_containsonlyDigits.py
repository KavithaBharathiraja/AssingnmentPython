#2.How to check if a String contains only digits?


str = "i love python coding123"

fount_digits = False

for char in str:
    if ('0' <= char <='9'):
        fount_digits = True
        break

if fount_digits:
    print("yes")
else:
    print("no")