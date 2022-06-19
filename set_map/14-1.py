N = int(input())
lst1 = list(map(int, input().split()))
nums = {}
# for i in lst1:
#     nums[i] = 1
nums = {i: 1 for i in (map(int, input().rstrip().split()))}
M = input()
lst2 = list(map(int, input().split()))

for i in lst2:
    if i in nums:
        print("1", end=" ")
    else:
        print("0", end=" ")
