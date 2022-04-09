n = 10000
number = [True for _ in range(n + 1)]
number[1] = False
for i in range(2, int(n**0.5) + 1):
    if number[i] == True:
        j = 2
        while True:
            if i * j > n:
                break
            number[i * j] = False
            j += 1

M = int(input())
N = int(input())
result_sum = 0
result_min = 0
for i in range(M, N + 1):
    if number[i]:
        if result_min == 0:
            result_min = i
        result_sum += i

if result_sum == 0:
    print(-1)
else:
    print(result_sum, result_min, sep="\n")
