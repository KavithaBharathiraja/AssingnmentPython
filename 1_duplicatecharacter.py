# 1.How to find duplicate characters in a String?

Str = "i love python coding"

Dict = {}

for char in Str:
    if char in Dict:
        Dict[char] += 1
    else:
        Dict[char] = 1

DuplicateChar = []
for char, count in Dict.items():
    if count > 1 and char != " ":
        DuplicateChar.append(char)

print(DuplicateChar)