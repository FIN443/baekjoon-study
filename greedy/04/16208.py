n = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst_sum = sum(lst)  # 14
result = 0
for i in lst:  # 2 3 4 5
    result += i * (lst_sum - i)
    lst_sum -= i
print(result)


""" 안좋은 예
(3 + 4)(5 + 2)
7 * 7 -> 3 * 4 + 5 * 2
49 + 12 + 10 = 71
"""

""" 그리디
a -> 2 * (3 + 4 + 5) = 24
b -> 3 * (4 + 5) = 27
c -> 4 * 5 = 20
a + b + c = 71
"""
