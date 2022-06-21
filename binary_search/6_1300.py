N = int(input())
k = int(input())

start = 1
end = N * N

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)
    if count >= k:
        end = mid - 1
    else:
        start = mid + 1
print(start)

""" 
1 2 3
2 4 6
3 6 9
0 1 2 3 2 5 6 3 6 9 
"""
