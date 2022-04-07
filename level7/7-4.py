import math


A, B, V = map(int, input().split())

print(math.ceil((V - A) / (A - B)) + 1)


""" 
5 1 6
5 4 / 9

5 1 20
5 4 / 9 8 / 13 12 / 17 16 / 21

4 2 7
4 2 / 6 4 / 8

4 2 13
4 2 / 6 4 / 8 6 / 10 8 / 12 10 / 14


(V-A / A-B).ceil   + 1 
"""
