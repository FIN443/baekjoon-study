N = int(input())

result = N // 5
last = N % 5
if N == 4 or N == 7:
    print(-1)
else:
    if last != 0:
        while True:
            if last % 3 == 0:
                result += last // 3
                break
            else:
                last += 5
                result -= 1
    print(result)
