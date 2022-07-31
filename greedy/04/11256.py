T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    box_size = []
    for _ in range(N):
        r, c = map(int, input().split())
        box_size.append(r * c)
    box_size.sort(reverse=True)

    count = 0
    left = J
    for i in box_size:
        left -= i
        count += 1
        if left <= 0:
            break

    print(count)
