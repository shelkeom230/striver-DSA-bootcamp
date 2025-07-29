import sys, re

sys.stdout = open("preprationSheet Sprint1 easy/output.txt", "w")
sys.stdin = open("preprationSheet Sprint1 easy/input.txt", "r")

# find n'th triangular number --> sum from 1 to n 
def findtriangular(n):
    sum=0
    for i in range(1,n+1):
        sum+=i 
    return sum

def find_train(n):
    return n*(n+1)//2
if __name__=="__main__":
    n = int(input())
    print(findtriangular(n)) 