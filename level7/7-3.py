n = int(input())

total = 1
count = 1
prev_total = 0
while n > total:
    count += 1
    prev_total = total
    total += count

last = n - prev_total
if count % 2 == 0:
    print(f"{last}/{(count + 1 - last)}")
else:
    print(f"{(count + 1 - last)}/{last}")


""" 
X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='') 
"""

"""
대각선으로 각 줄을 나눠서 보면 [1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1] 이렇게 나타낼 수 있다. 

따라서, 입력받은 X를 1씩 늘려 가며 빼서 몇 번째 줄에 몇 번째 숫자인지 구하고 짝수번 째 줄인지 홀수번째 줄인지에 따라 
분자, 분모의 숫자의 방향이 홀수 줄인 경우 분자는 내림차순, 분모는 오름차순이고, 짝수 줄인 경우 그 반대이다.
"""
