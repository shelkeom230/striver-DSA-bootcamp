def findFact(n):
    if n==0: return 1 
    return n*findFact(n-1)

def findFactIterative(n):
    factval=1 
    
    for i in range(1,n+1):
        factval*=i 
    return factval 

n=int(input())
print(findFactIterative(n))