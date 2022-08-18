# 열차 시간표(Large)
import heapq

N = int(input())
for page in range(N):
    T = int(input())
    NA, NB = map(int, input().split())
    trips = []
    for _ in range(NA):
        s, e = input().split()
        h1, m1 = map(int, s.split(":"))
        h2, m2 = map(int, e.split(":"))
        trips.append([h1 * 60 + m1, h2 * 60 + m2, 0])
    for _ in range(NB):
        s, e = input().split()
        h1, m1 = map(int, s.split(":"))
        h2, m2 = map(int, e.split(":"))
        trips.append([h1 * 60 + m1, h2 * 60 + m2, 1])

    trips.sort()

    start = [0, 0]
    trains = [[], []]

    for trip in trips:
        d = trip[2]
        if trains[d] and trains[d][0] <= trip[0]:
            heapq.heappop(trains[d])
        else:
            start[d] += 1
        heapq.heappush(trains[1 - d], trip[1] + T)

    print(f"Case #{page+1}: {start[0]} {start[1]}")
