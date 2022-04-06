i_char = list(map(str, input()))
i_int = list(map(ord, i_char))
ascii_char = list(map(chr, list(range(97, 97 + 26))))
ascii_int = [-1 for _ in range(26)]
count = 0
for i in i_int:
    ascii_int[i - 97] = i_int.index(i)
print(*ascii_int, sep=" ")
