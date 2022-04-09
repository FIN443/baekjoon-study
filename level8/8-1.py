n = 1000
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

""" 
list1=[True]*(y+1)
m=int(y**0.5)
for i in range(2,m+1):
    if list1[i]==True:
        for j in range(i+i,y+1,i):
            list1[j]=False
"""

n = int(input())
inputs = list(map(int, input().split()))
result = 0
for i in inputs:
    if number[i]:
        result += 1

print(result)
