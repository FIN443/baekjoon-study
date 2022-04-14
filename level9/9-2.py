def fibo(n):
    return fibo(n - 1) + fibo(n - 2) if n > 1 else n


print(fibo(int(input())))
