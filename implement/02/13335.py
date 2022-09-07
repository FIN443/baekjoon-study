# 트럭
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0 for _ in range(w)]  # 다리에 que 적용
weight, time = 0, 0
while bridge:
    a = bridge.pop(0)
    weight -= a

    if trucks:
        if weight + trucks[0] <= L:
            bridge.append(trucks[0])
            weight += trucks[0]
            trucks.pop(0)
        else:
            bridge.append(0)
    time += 1

print(time)
