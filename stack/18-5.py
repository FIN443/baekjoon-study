N = int(input())
nums = [int(input()) for _ in range(N)]
stack = []
result = []
prev = 0
for n in nums:
    if not stack or stack[-1] != n:
        for i in range(prev + 1, n + 1):
            stack.append(i)
            result.append("+")
        prev = stack[-1]
    if stack and stack[-1] == n:
        stack.pop()
        result.append("-")
    else:
        break

if stack:
    print("NO")
else:
    print(*result, sep="\n")
