# 물병
N, K = map(int, input().split())
count = 0

""" 
while bin(N).count("1") > K:
    N += 1
    count += 1 
"""

while bin(N).count("1") > K:
    idx = bin(N)[::-1].index("1")
    count += 2**idx
    N += 2**idx

print(count)
