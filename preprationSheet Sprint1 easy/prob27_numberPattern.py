import sys,re
sys.stdout=open("preprationSheet Sprint1 easy/output.txt","w")
sys.stdin=open("preprationSheet Sprint1 easy/input.txt","r")


# generate number pattern 
def pattern(r):
    n=1
    for i in range(1,r+1):
        for j in range(1,r+1):
            print(n,end=" ")
            n+=1
        print()
        
if __name__=="__main__":
    n=int(input())
    pattern(n)