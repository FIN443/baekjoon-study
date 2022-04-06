def isValid(m):
    isExists = False
    for i in m:
        if max(m) == i:
            if isExists == True:
                return False
            else:
                isExists = True
    return True


i_char = list(map(str, input()))
i_int = list(map(ord, i_char))
ascii_int = [0 for _ in range(26)]
for i in i_int:
    if i < 97:
        ascii_int[i - 65] += 1
    else:
        ascii_int[i - 97] += 1

if not isValid(ascii_int):
    print("?")
else:
    print(chr(ascii_int.index(max(ascii_int)) + 65))
