# 4.How to remove duplicate characters from String?

Str = "i love python coding"

Dict = {}

for char in Str:
    if char in Dict:
        Dict[char] += 1;
    else:
        Dict[char] = 1;

char_list = list(Dict.keys())

for char, count in Dict.items():
    if count > 1 and char in char_list:
        char_list.remove(char)
print(char_list)