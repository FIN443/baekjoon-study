# 백준 8-6 9020번 골드바흐의 추측

# 4 <= n <= 10000
# T <- 테스트 케이스
# n <- 짝수
n = 10000
number = [True for _ in range(n + 1)]
number[1] = False
for i in range(2, int(n**0.5) + 1):
    if number[i] == True:
        for j in range(i + i, n + 1, i):
            number[j] = False
T = int(input())
results = []
for i in range(T):
    n = int(input())
    for j in range(n // 2, 10001):
        if number[j]:
            n -= j
            if number[n]:
                results.append([n, j])
                break
            else:
                n += j
for result in results:
    print(*result, sep=" ")

"""다른 답안
prime_number = [0 for _ in range(10001)]
prime_number[1] = 1

# 에라토스테네스의 체
for i in range(2,int(10000**0.5) + 1):
    if prime_number[i] == 0:
        for j in range(i+i,10001,i):
            prime_number[j] = 1

T = int(sys.stdin.readline())
for _ in range(T):
    # 2보다 큰 짝수가 주어진다
    n = int(sys.stdin.readline())
    
    # 짝수의 절반부터 감소해가며 판단
    m = n // 2
    for i in range(m,1,-1):
        # 만약 현재 숫자가 소수고, n-i 즉 더해지는 수도 소수면 print 후 출력
        if prime_number[i] == 0 and prime_number[n-i] == 0:
            print(i,n-i)
            break
"""
