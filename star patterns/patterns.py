import sys
sys.stdout=open("star patterns/output.txt","w")
sys.stdin=open("star patterns/input.txt","r")


def print1(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
def print2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
def print3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def print4(n):
    for i in range(n+1):
        for j in range(i):
            print(i,end=" ")
        print()
def print5(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end=" ")
        print()                 
def print6(n):
    for i in range(n):
        for j in range(1,(n-i+1)):
            print(j,end=" ")
        print()
def print7(n):
   for i in range(n):
        #    space 
        for j in range(n-i-1): 
            print(" ",end="")
        
        # stars 
        for j in range(2*i+1):
            print("*",end="")
        
        # space 
        for j in range(n-i-1):
            print(" ",end="")
        print()
def print8(n):
    for i in range(n):
        # space 
        for j in range(i):
            print(" ",end="")
        
        # stars 
        for j in range(2*n-(2*i+1)):
            print("*",end="")
        
        # space 
        for j in range(i):
            print(" ",end="")
        print()
def print11(n):
    start=1 
    for i in range(1,n+1):
        if i%2==0: start=0
        else: start=1 
        for j in range(i):
            print(start,end="")
            start=1-start
        print()
def print12(n):
    for i in range(1,n+1):
        # nums 
        for j in range(1,i+1):
            print(j,end="")
            
        # spaces 
        for j in range(2*(n-i)):
            print(" ",end="")
        # nums
        for j in range(i,0,-1):
            print(j,end="")
        print() 
def print13(n):
    num=1 
    for i in range(n):
        for j in range(i+1):
            print(num,end="")
            num+=1
        print()
def print14(n):
    for i in range(n):
        for ch in range(ord('A'),ord('A')+i+1):
            print(chr(ch),end="")
        print() 
def print15(n):
    for i in range(n):
        for ch in range(ord('A'),ord('A')+(n-i)):
            print(chr(ch),end="")
        print()       
def print16(n):
    for i in range(n):
        for j in range(i+1):
            print((chr)(ord('A')+i),end=" ")
        print()
def print17(n):
    for i in range(n):
        # spaces 
        for j in range(n-i-1):
            print(" ",end="")
        
        # chars 
        ch='A'
        breakpoint=(2*i+1)//2
        for j in range(1,(2*i+2)):
            print(ch,end="")
            if j<=breakpoint: ch=chr(ord(ch)+1)
            else: ch=chr(ord(ch)-1)
        
        # space 
        for j in range(n-i-1):
            print(" ",end="")
        print()
def print18(n):
    for i in range(n):
        # chars 
        for ch in range(ord('A')+n-1-i,ord('A')+n):
            print(chr(ch),end=" ")
        print() 
def print18_1(n):
    for i in range(n):
        for ch in range(ord('A')+n-1,ord('A')+n-2-i,-1):
            print(chr(ch),end=" ")
        print()
def print19(n):
    inis=0
    for i in range(n):
        # stars 
        for j in range(n-i):
            print("*",end="")
        
        # spaces 
        for j in range(inis):
            print(" ",end="")
        
        # stars
        for j in range(n-i):
            print("*",end="") 
        inis+=2
        print()
    
    # 2nd half 
    inis=2*n-2 
    for i in range(1,n+1):
        # stars
        for j in range(1,i+1):
            print("*",end="")
        
        # spaces 
        for j in range(inis):
            print(" ",end="")
        
        # stars 
        for j in range(1,i+1):
            print("*",end="")
        inis-=2
        print()
def print20(n):
    spaces=2*n-2
    for i in range(1,2*n):
        # upper half 
        stars=i 
        
        # lower half 
        if i>n: stars=2*n-i 
        
        # stars 
        for j in range(1,stars+1):
            print("*",end="")
        
        # spaces 
        for j in range(1,spaces+1):
            print(" ",end="")
            
        # stars 
        for j in range(1,stars+1):
            print("*",end="")
        print()
        if i<n: spaces-=2
        else: spaces+=2
def print21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1: 
                print("*",end="")
            else: 
                print(" ",end="")
        print()
def print22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top,left,right,bottom=i,j,(2*n-1)-1-j,(2*n-1)-1-i 
            print(n-min(min(left,right),min(top,bottom)),end="")
        print()            
if __name__=="__main__":
    n=int(input())
    print22(n)