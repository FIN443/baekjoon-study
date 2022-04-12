# x, y, w, h
# (x, y) 한수
# 왼쪽 아래 꼭짓점 (0, 0)
# 오른쪽 위 꼭짓점 (w, h)
# 1<=x<=w-1

x, y, w, h = map(int, input().split())
if x > w // 2:
    x = w - x
if y > h // 2:
    y = h - y
print(min(x, y))

"""다른 답안
x,y,w,h = map(int,input().split())
print(min(w-x,h-y,x,y))
"""
