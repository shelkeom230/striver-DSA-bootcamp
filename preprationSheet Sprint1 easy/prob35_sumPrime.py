import sys, math as m 

sys.stdout = open("preprationSheet Sprint1 easy/output.txt", "w")
sys.stdin = open("preprationSheet Sprint1 easy/input.txt", "r")
def checkPrime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0: cnt+=1
    
    if cnt==2: 
        return True
    else:
        return False 
     
def sumPrime(low,high):
    sum=0
    for i in range(low,high+1):
        if checkPrime(i):
            sum+=i 
    return sum 

if __name__=="__main__":
    low=int(input())
    high=int(input())
    
    print(sumPrime(low,high))
    