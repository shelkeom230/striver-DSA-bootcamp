# write a program to print pyramid pattern 
def printPyramid1(n):
    for i in range(n):
            
        # spaces 
        for j in range(n-i-1):
            print(" ",end="")
        
        # stars 
        for j in range(2*i+1):
            print("*",end="")
        
        # spaces
        for j in range(n-i-1):
            print(" ",end="")

        print()
    
def printPyramid2(n):
    for i in range(n):
        # spaces 
        for j in range(i):
            print(" ",end="")
        
        # stars 
        for j in range(2*n-(2*i+1)):
            print("*",end='')
        
        # sapces 
        for j in range(i):
            print(" ",end="")
        print()

def printPyramid(n):
    printPyramid1(n)
    printPyramid2(n)

n=int(input())
printPyramid(n)