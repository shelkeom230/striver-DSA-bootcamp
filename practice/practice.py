# binary search on grids
import sys, threading

def revSentence(sen):
    ans=""
    lastWord=0
    for i in range(len(sen)-1,-1,-1):
        if sen[i]==' ':
            ans+=sen[lastWord:i+1]
            ans+=' '
            lastWord=i+1 
    return ans 

def grid(mat,x,y,k):
    n=len(mat)
    m=len(mat[0])

    for i in range(x,n):
        for j in range(y,n):
            if k&1==0:
                mat[i][j],mat[i+1][j]=mat[i+1][j],mat[i][j]
            else:
                mat[i][j],mat[i+(k-1)][j]=mat[i+(k-1)][j],mat[i][j]
    return mat 
def main():
    sys.stdin = open("practice/input.txt", "r")
    sys.stdout = open("practice/output.txt", "w")
    input = sys.stdin.readline

    # start here
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    x,y,k=list(map(int,input().split()))
    print(grid(mat,x,y,k))
threading.Thread(target=main).start()
