word_sheet = ["c=", "c-", "d-", "dz=", "lj", "nj", "s=", "z="]

word = input()
result = 0
for i in word_sheet:
    word = word.replace(i, "0")
print(len(word))
