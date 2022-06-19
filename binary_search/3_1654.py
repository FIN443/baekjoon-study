K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

start = 1
end = max(lst)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in lst:
        count += i // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
