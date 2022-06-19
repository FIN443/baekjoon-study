def hanoi(n, source, to, other):
    if n == 1:
        print(source, to)
        return
    hanoi(n - 1, source, other, to)
    print(source, to)
    hanoi(n - 1, other, to, source)


n = int(input())

print(2**n - 1)
# 1번(출발지), 3번(목적지), 2번(나머지)
hanoi(n, 1, 3, 2)

""" 
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
"""
