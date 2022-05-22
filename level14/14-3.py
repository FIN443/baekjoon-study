N, M = map(int, input().split())
lst = [input() for _ in range(N)]
pokemons_nums = {i + 1: value for i, value in enumerate(lst)}
pokemons_names = {value: i + 1 for i, value in enumerate(lst)}
answers = [input() for _ in range(M)]

for i in answers:
    if i.isdigit():  # isnumeric()
        print(pokemons_nums[int(i)])
    else:
        print(pokemons_names[i])
