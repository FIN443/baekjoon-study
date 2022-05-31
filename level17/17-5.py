N = int(input())
road_lens = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.pop()

prev_price = 1000000001
final_price = 0
for p, l in zip(prices, road_lens):
    if prev_price > p:
        prev_price = p
    final_price += prev_price * l
print(final_price)
