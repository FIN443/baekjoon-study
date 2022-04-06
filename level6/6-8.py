value_sheet = [
    "ABC",
    "DEF",
    "GHI",
    "JKL",
    "MNO",
    "PQRS",
    "TUV",
    "WXYZ",
]
word = input()
result = 0
for i in word:
    for j in value_sheet:
        if i in j:
            result += value_sheet.index(j) + 3
print(result)
