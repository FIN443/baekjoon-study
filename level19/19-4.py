T = int(input())

for _ in range(T):
    answer = 0
    total, location = map(int, input().split())
    priorities = list(map(int, input().split()))

    p = [(p, i) for i, p in enumerate(priorities)]
    # print(max(p, key=lambda x: x[0]))
    lst = []
    while True:
        if len(p) == 0:
            break
        # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        j = p.pop(0)
        # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if p and max(p, key=lambda x: x[0])[0] > j[0]:
            p.append(j)
        # 3. 그렇지 않으면 J를 인쇄합니다.
        else:
            lst.append(j)

    for i, c in enumerate(lst):
        if c[1] == location:
            answer = i + 1
    print(answer)
