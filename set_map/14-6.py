N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))


""" ???
_=input
_()
v=lambda:{*map(int,_().split())}
a=v()
b=v()
print(len(a-b)+len(b-a))
"""
