import sys,re
sys.stdout=open("preprationSheet Sprint1 easy/output.txt","w")
sys.stdin=open("preprationSheet Sprint1 easy/input.txt","r")

# find the largest palindromic substring
def findSubs(s):
    res=""
    resLen=0
    
    for i in range(len(s)):
        # odd length 
        l,r=i,i
        
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>resLen:
                res=s[l:r+1]
                resLen=r-l+1
            l-=1
            r+=1
        
        # even length 
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>resLen:
                res=s[l:r+1]
                resLen=r-l+1
            l-=1
            r+=1
    return res 

str=input()
print(findSubs(str))