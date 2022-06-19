import sys
from collections import Counter


T = int(input())
counter = Counter()
for _ in range(T):
    counter[int(sys.stdin.readline())] += 1

results = sorted(counter.items(), key=lambda x: x[0])
# results = sorted(counter.most_common())

for i in results:
    for _ in range(i[1]):
        print(i[0])


""" 
import sys
input=sys.stdin.readline

N = int(input())
num_list = [0] * 10001

for i in range(N): #append를 사용하면 메모리 재할당이 이루어져 비효율적임
    new = int(input())
    num_list[new] += 1

for j in range(len(num_list)):
    if num_list[j] != 0:
        for g in range(num_list[j]):
            print(j)
"""
