def compact(lst):
    return list(filter(None, lst))


lst = [0, 1, False, 2, "", 3, "a", "s", 34]
print(compact(lst))
