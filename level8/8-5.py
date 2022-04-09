n = 123456 * 2
number = [True for _ in range(n + 1)]
number[1] = False
for i in range(2, int(n**0.5) + 1):
    if number[i] == True:
        j = 2
        while True:
            if i * j > n:
                break
            number[i * j] = False
            j += 1

results = []
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if number[i]:
            count += 1
    results.append(count)
print(*results, sep="\n")


""" 
prime_list = [True] * (250000)
prime_list[0] = False
prime_list[1] = False
    
for a in range(len(prime_list)):
    if prime_list[a]:
    	for i in range(a*2, 250000, a):
	    	prime_list[i] = False
while True:
    number = int(input())
    if number == 0:
        break

    print(prime_list[number+1:number*2+1].count(True))
"""
