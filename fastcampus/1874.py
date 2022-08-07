# 스택 수열
n = int(input())
lst = [int(input()) for _ in range(n)]
nums = []

pos = 0
result = []
for i in lst:
    if pos < i:
        while pos != i:
            pos += 1
            nums.append(pos)
            result.append("+")

    if nums.pop() != i:
        print("NO")
        exit()
    result.append("-")

print(*result, sep="\n")
