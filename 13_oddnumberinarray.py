# 13. Given an array of integers, print only odd numbers array[]={3,8,6,14,5,17,19}

array =[3, 8, 6, 14, 5, 17, 19]

oddnum = []

for num in array:
    if num % 2 != 0:
        oddnum.append(num)
print(oddnum)