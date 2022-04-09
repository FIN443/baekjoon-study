N = int(input())
for i in range(2, N + 1):
    if N > 0:
        while N % i == 0:
            N = N / i
            print(i)
    else:
        break
