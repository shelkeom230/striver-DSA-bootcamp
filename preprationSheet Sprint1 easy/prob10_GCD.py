# find GCD of 2 numbers 
def findGCD(n1,n2):
    gcd=1
    for i in range(1,min(n1,n2)):
        if n1%i==0 and n2%i==0: gcd=i
    print(gcd)

def findGCD2(n1,n2):

    for i in range(min(n1,n2),0,-1):
        if n1%i==0 and n2%i==0: 
            print(i)
            break 

# most optimal appraoch 
def findGCDOptimal(n1,n2):
    while n1>0 and n2>0:
        if n1>n2: n1=n1%n2 
        else: n2=n2%n1 
    
    if n1==0: return n2 
    return n1 

print(findGCDOptimal(25,30))
        