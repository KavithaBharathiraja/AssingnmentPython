# 3.How to count a number of vowels and consonants in a String?

Str = "i love python coding"

vowels= "aeiouAEIOU"
vowels_count =0
consonants_count =0

for char in Str:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print("vowels_count: " , vowels_count)
print("consonants_count: " , consonants_count)