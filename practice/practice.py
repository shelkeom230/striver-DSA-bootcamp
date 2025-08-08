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
def main():
    # sys.stdin = open("practice/input.txt", "r")
    # sys.stdout = open("practice/output.txt", "w")
    input = sys.stdin.readline

    # start here
    string="123456"
    lst=[int(char) for char in string]
    print(lst)
threading.Thread(target=main).start()
