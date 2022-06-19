T = int(input())
lst = []
for _ in range(T):
    n = int(input())
    cnt0 = [1, 0, 1]
    cnt1 = [0, 1, 1]
    l = len(cnt0)
    if n >= l:
        for i in range(l, n + 1):
            cnt0.append(cnt0[i - 1] + cnt0[i - 2])
            cnt1.append(cnt1[i - 1] + cnt1[i - 2])
    lst.append((cnt0[n], cnt1[n]))

for i, j in lst:
    print(i, j)
