import math as m 
# check if a number is prime or not 
def checkPrime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0: cnt+=1
    
    if cnt==2: print("yes")
    else: print("no")
    
# optimised approach (only go from 2 to sqrt(n))
def checkPrime2(n):
    if n<2: return False 
    else:
        for i in range(2,(int)(m.sqrt(n))+1):
            if n%i==0: return False 
    return True 

# most optimised approach 
def checkPrime3(n):
    cnt=0
    for i in range(1,(int)(m.sqrt(n))+1):
        if n%i==0:
            cnt+=1
            if (n//i)!=i:
                cnt+=1
    if cnt==2: return True 
    else: return False 
    
n=int(input())
print(checkPrime3(n))