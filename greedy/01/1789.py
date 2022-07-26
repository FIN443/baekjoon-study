S = int(input())

n_sum = 0
n = 1
count = 0
while n_sum <= S:
    n_sum += n
    n += 1
    count += 1

print(count - 1)
