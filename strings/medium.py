# strings medium problems 
import sys, threading
from collections import Counter,defaultdict

# sort string by freq of chars - 0(klogk)
def sortString(string):
    freq={}
    for char in string:
        freq[char]=freq.get(char,0)+1

    # sort the dict by values desc 
    sorted_list=sorted(freq.items(),key=lambda item: item[1], reverse=True)
    
    # append char in the resuult 
    res=[]
    for char,count in sorted_list:
        if char!=' ':
            res.append(char*count)
    return ''.join(res) 

# sort string by freq of chars - better
def sortStringBetter(string):
    count=Counter(string) # char-> cnt 
    buckets=defaultdict(list) # cnt-> [char]

    # fill the buckets dict 
    for char,cnt in count.items():
        buckets[cnt].append(char)
    
    res=[]
    for i in range(len(string),0,-1):
        for char in buckets[i]:
            if char!=' ':
                    
                res.append(char*i)
    
    return "".join(res)

# maximum nesting depth of parentheses -- using stack 
def maxDepthStack(string):
    stack=[]
    maxDepth=0 

    for char in string:
        if char=='(':
            stack.append(char)
            maxDepth=max(maxDepth,len(stack))
        elif char==')':
            if stack:
                stack.pop()
    return maxDepth   

# maximum nesting depth of parentheses -- without stack 
def maxDepthWithoutStack(string):
    depth=0
    maxDepth=0
    for char in string:
        if char=='(':
            depth+=1
            maxDepth=max(maxDepth,depth)
        elif char==')':
            depth-=1
    return maxDepth 

# roman to integer conversion -- optimal  
def romanToIntConv(romanstr):
    value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

    integer=0
    n=len(romanstr)
    for i in range(n):
        if i<n-1 and value[romanstr[i]]<value[romanstr[i]]:
            integer-=value[romanstr[i]]
        else:
            integer+=value[romanstr[i]]
    return integer 

# implement atoi (string to integer)
def atoi(string):
    # remove left whitespaces 
    string=string.lstrip()

    if not string:
        return 0
    # determine the sign and start from the first digit
    sign=1
    i=0

    if string[0]=='-':
        sign-=2
        i+=1
    if string[0]=='+':
        i+=1
    
    num=0
    # store the result until we find a non-digit 
    while i<len(string) and string[i].isdigit():
        num=num*10+int(string[i])
        i+=1
    
    # add the sign 
    num*=sign 

    # handle the range 
    INT_MIN=-2**31 
    INT_MAX=+2**31-1 

    if num<INT_MIN:
        return INT_MIN 
    elif num>INT_MAX:
        return INT_MAX 
    return num 

# count number of substrings -- brute force
def cntSubstrings(string):
    n=len(string)

    cnt=0
    for i in range(n):
        for j in range(i+2,n):
            substr=string[i:j+1]
            if 'a' in substr and 'b' in substr and 'c' in substr: 
                cnt+=1
    
    return cnt 

# count number of substrings -- optimal 1 
def cntSubstrOptimal(string):
    n=len(string)
    count={'a':0,'b':0,'c':0}
    ans=0
    left=0

    for right in range(n):
        count[string[right]]+=1

        while count['a']>0 and count['b']>0 and count['c']>0:
            ans+=(n-right)
            count[string[left]]-=1
            left+=1
    return ans  

# count number of substrings -- optimal 2 
def cntSubstringsOptimal(string):
    n=len(string)
    lastSeen=[-1,-1,-1]
    cnt=0

    for i in range(n):
        lastSeen[ord(string[i])-ord('a')]=i 

        if lastSeen[0]!=-1 and lastSeen[1]!=-1 and lastSeen[2]!=-1:

            cnt+=(1+min(lastSeen[0],lastSeen[1],lastSeen[2]))
    return cnt 

# longest palindromic substring -- brute 
def longPalindromicSubstrBrute(string):
    n=len(string)

    maxLength=0
    best_substr="" 
    for i in range(n):
        for j in range(i,n):
            substr=string[i:j+1]
            if substr==substr[::-1]:
                if len(substr)>maxLength:
                    maxLength=len(substr)
                    best_substr=substr 
    return best_substr 

# longest palindromic substring -- optimal 
def longestPalindromicOptimal(string):
    n=len(string)
    resLen=0
    res="" 

    for i in range(n):
        left,right=i,i 

        # odd length 
        while left>=0 and right<n and string[left]==string[right]:
            if(right-left+1)>resLen:
                res=string[left:right+1]
                resLen=right-left+1
            left-=1
            right+=1
        
        # even length 
        left,right=i,i+1 
        while left>=0 and right<n and string[left]==string[right]:
            if(right-left+1)>resLen:
                res=string[left:right+1]
                resLen=right-left+1
            left-=1
            right+=1
    return res 

# sum of beauty of all substrings -- brute 
def sumBeautyBrute(string):
    n=len(string)

    sumVal=0

    for i in range(n):
        freq={}
        for j in range(i,n):
            for k in range(i,j+1):
                freq[string[k]]=freq.get(string[k],0)+1
            
            minFreq,maxFreq=0,0

            for val in freq.values():
                minFreq=min(minFreq,val)
                maxFreq=max(maxFreq,val)
            
            if maxFreq-maxFreq!=0:
                sumVal+=(maxFreq-minFreq)
    return sumVal 

def main():
    sys.stdin = open("strings/input.txt", "r")
    sys.stdout = open("strings/output.txt", "w")
    input = sys.stdin.readline  

    # start here
    # s,t = list(map(str,input().split()))
    string=input()

    print(sumBeautyBrute(string))
threading.Thread(target=main).start()