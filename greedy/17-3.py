def accumulate_tuple_key(lst):
    accum = 0
    for _, i in lst:
        accum += i
        yield accum


N = int(input())
time = list(map(int, input().split()))
waiting = [(i + 1, t) for i, t in enumerate(time)]
waiting.sort(key=lambda x: x[1])
print(sum(list(accumulate_tuple_key(waiting))))
