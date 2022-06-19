def print_star(n):
    if n == 1:
        return ["*"]

    stars = print_star(n // 3)
    # print(f"n={n}")
    result = []
    # 복제하면서 생성
    for star in stars:
        result.append(star * 3)
        # print(1, *result, sep="\n")
    for star in stars:
        result.append(star + " " * (n // 3) + star)
        # print(2, *result, sep="\n")
    for star in stars:
        result.append(star * 3)
        # print(3, *result, sep="\n")

    return result


n = int(input())
print(*print_star(n), sep="\n")
