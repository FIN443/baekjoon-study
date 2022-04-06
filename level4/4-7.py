def solution(m):
    return True if m > row_avg else False


n = int(input())
row_list = []
for _ in range(n):
    row = list(map(int, input().split()))
    row_n = row.pop(0)
    row_avg = round((sum(row) / row_n), 3)
    row_result = len(list(filter(solution, row)))
    row_list.append(round((row_result / row_n) * 100, 3))
for item in row_list:
    print("{:.3f}%".format(item))
