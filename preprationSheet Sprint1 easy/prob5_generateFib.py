# genearate fib sequence upto limit l 
def findFib(n):
    if n<=1: return n 
    return findFib(n-1)+findFib(n-2)

def generateFib(n):
    i=0
    while findFib(i)<=n:
        print(findFib(i))
        i+=1
        
    
n=int(input())
generateFib(n)
    