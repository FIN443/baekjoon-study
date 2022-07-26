N, M = map(int, input().split())  # 스크린 크기, 바구니 면적
apple_num = int(input())

left = 1
right = M
result = 0

for _ in range(apple_num):
    apple = int(input())
    if left <= apple <= right:  # 바구니 안에 떨어질 때
        continue

    if left > apple:  # 바구니 왼쪽에 떨어질 때
        result += left - apple
        right -= left - apple
        left = apple

    else:  # 바구니 오른쪽에 떨어질 때
        result += apple - right
        left += apple - right
        right = apple

print(result)
