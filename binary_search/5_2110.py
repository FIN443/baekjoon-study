import sys


input = sys.stdin.readline
N, C = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
result = 0
start = 1
end = lst[-1] - lst[0]
while start <= end:
    mid = (start + end) // 2
    prev = lst[0]
    count = 1
    for i in range(1, len(lst)):
        if lst[i] >= prev + mid:
            count += 1
            prev = lst[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
