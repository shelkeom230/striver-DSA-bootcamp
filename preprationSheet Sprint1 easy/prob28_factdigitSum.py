import sys,re
sys.stdout=open("preprationSheet Sprint1 easy/output.txt","w")
sys.stdin=open("preprationSheet Sprint1 easy/input.txt","r")

# find sum of digits of factorial of a number
def findFact(n):
    if n==0: return 1
    return n*findFact(n-1)
 
def findSum(n):
    factval=findFact(n)
    sum=0
    while(factval>0):
        digit=factval%10
        sum+=digit 
        factval//=10
    return sum 

if __name__=="__main__":
    n=int(input())
    print(findSum(n))
    