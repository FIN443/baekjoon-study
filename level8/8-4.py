n = 1000000
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
M, N = map(int, input().split())
for i in range(M, N + 1):
    if number[i]:
        print(i)

""" 
def find_num(x,y):
    list1=[True]*(y+1)
    m=int(y**0.5)
    for i in range(2,m+1):
        if list1[i]==True:
            for j in range(i+i,y+1,i):
                list1[j]=False
    return [i for i in range(2,y+1) if list1[i]==True and i>=x]


num1,num2=map(int,input().split())

for i in find_num(num1,num2):
    print(i)
"""
