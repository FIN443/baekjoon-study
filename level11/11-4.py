from collections import Counter
import sys

T = int(sys.stdin.readline())
lst = []
for _ in range(T):
    lst.append(int(sys.stdin.readline()))
# print("---")
lst = sorted(lst)
lst_c = Counter(lst).most_common()
# lst_c = sorted(Counter(lst).items(), key=lambda x: x[0])
# 산술평균
print(int(round(sum(lst) / T, 0)))
# 중앙값
print(lst[T // 2])
# 최빈값
if len(lst_c) > 1:
    if lst_c[0][1] == lst_c[1][1]:
        print(lst_c[1][0])
    else:
        print(lst_c[0][0])
else:
    print(lst_c[0][0])
# 범위(최댓값-최솟값)
print(lst[-1] - lst[0])
