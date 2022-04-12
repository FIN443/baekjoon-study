coords_x = []
coords_y = []
for _ in range(3):
    n, m = map(int, input().split())
    coords_x.append(n)
    coords_y.append(m)
if coords_x.count(max(coords_x)) % 2 == 1:
    x = max(coords_x)
else:
    x = min(coords_x)
if coords_y.count(max(coords_y)) % 2 == 1:
    y = max(coords_y)
else:
    y = min(coords_y)
print(x, y)

"""다른 답안
x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4) 
"""
