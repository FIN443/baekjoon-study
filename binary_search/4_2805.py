N, M = map(int, input().split())

lst = list(map(int, input().split()))

start = 1
end = max(lst)
while start <= end:
    mid = (start + end) // 2
    height_sum = 0
    for i in lst:
        if mid < i:
            height_sum += i - mid

    if height_sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
