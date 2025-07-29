# ways to take array input 

n=5
# int list → 1 2 3
arr = list(map(int, input().split()))

# string list → a b c
arr = input().split()

# char list → abc
arr = list(input())

# multiple lines → 1 per line
arr = [int(input()) for _ in range(n)]

# 2D array input 
matrix=list(map(int,input().split()) for _ in range(n))