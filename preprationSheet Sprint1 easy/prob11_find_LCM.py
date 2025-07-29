import math as m 
# find LCM of 2 numbers 
def findLCM1(n1,n2):
    maxnum=max(n1,n2)
    while True:
        if maxnum%n1==0 and maxnum%n2==0:
            return maxnum
        maxnum+=1
        
# quite optimal way 
def findLCM2(n1,n2):
    return abs(n1*n2)//m.gcd(n1,n2)

n1,n2=int(input()),int(input())
print(findLCM2(10,20))