# 햄버거 분배
N, K = map(int, input().split())
table = list(input())
pos = 0
count = 0
while True:
    if pos >= len(table) - 1:
        break

    if table[pos] == "P":
        for i in range(pos + 1, K + pos + 1):
            if i < len(table) and table[i] == "H":
                table[i] = "X"
                count += 1
                break
    elif table[pos] == "H":
        for i in range(pos + 1, K + pos + 1):
            if i < len(table) and table[i] == "P":
                table[i] = "X"
                count += 1
                break
    pos += 1

print(count)
