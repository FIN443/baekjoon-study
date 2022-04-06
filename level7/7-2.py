n = int(input())

if n == 1:
    print(1)
else:
    count = 0
    while True:
        if n <= count * (3 * (count - 1)) + 1:
            break
        count += 1
    print(count)

# 모범 답안
""" 
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt) 
"""

# a1 = 1*0
# a2 = 2*3
# a3 = 3*6
# a4 = 4*9
# a5 = 5*12
# a6 = 6*15
