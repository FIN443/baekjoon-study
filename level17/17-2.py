N = int(input())
time = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append((a, b))
time.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for a, b in time:
    if a >= end_time:
        count += 1
        end_time = b
print(count)
