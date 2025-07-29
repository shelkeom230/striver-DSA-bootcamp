import sys, math as m 
sys.stdout=open("preprationSheet Sprint1 easy/output.txt","w")
sys.stdin=open("preprationSheet Sprint1 easy/input.txt","r")

# generate pascal's traingle 
def gen(n):
    res=[[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i:
                res[i][j]=1
            else:
                res[i][j]=res[i-1][j]+res[i-1][j-1]
    
    # print the result 
    for i in range(n):
        for j in range(i+1):
            print(res[i][j],end=' ')
        print()

# using formula 
def pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(m.comb(i,j),end=' ')
        print()
    
# calculate manually 
def pascal2(n):
    for i in range(n):
        for j in range(i+1):
            res=m.factorial(i)/(m.factorial(j)*m.factorial(i-j))
            print(int(res),end=' ')
        print()
        
n=int(input())
pascal2(n)
    
    