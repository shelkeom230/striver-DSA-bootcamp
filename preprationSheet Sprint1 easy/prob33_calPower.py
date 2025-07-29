import sys, re

sys.stdout = open("preprationSheet Sprint1 easy/output.txt", "w")
sys.stdin = open("preprationSheet Sprint1 easy/input.txt", "r")


# calculate a power b
def calPower1(a, b):
    res = 1
    while b>0:
        if b%2==1: res*=a 
        a*=a 
        b//=2
    
    return res 

# use divide and conquer 
def calPower2(a,b):
    if b==0: return 1 
    
    temp=calPower2(a,b//2)
    res=temp*temp 
    if b%2==1: res*=a 
    return res 

if __name__=="__main__":
    a,b=int(input()),int(input())
    
    print(calPower1(a,b))