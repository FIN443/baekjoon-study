N = int(input())
lst = []

for i in range(N):
    lst.append(int(input()))

target = lst[0]
candi = lst[1:]

if N == 1:
    print(0)
else:
    count = 0
    candi.sort(reverse=True)
    while candi[0] >= target:
        candi[0] -= 1
        target += 1
        count += 1
        candi.sort(reverse=True)

    print(count)
