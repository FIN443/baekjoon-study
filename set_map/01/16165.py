# 걸그룹 마스터 준석이
import sys
from collections import defaultdict


input = sys.stdin.readline
team_dict = defaultdict(list)
member_dict = {}
N, M = map(int, input().split())
for _ in range(N):
    team = input().rstrip()
    k = int(input())
    for _ in range(k):
        name = input().rstrip()
        team_dict[team].append(name)
        member_dict[name] = team
    team_dict[team].sort()

result = []
for _ in range(M):
    v = input().rstrip()
    opt = int(input())
    if opt == 0:
        for i in team_dict[v]:
            result.append(i)
    elif opt == 1:
        result.append(member_dict[v])

print(*result, sep="\n")
