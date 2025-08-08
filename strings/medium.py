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
    
def main():
    sys.stdin = open("strings/input.txt", "r")
    sys.stdout = open("strings/output.txt", "w")
    input = sys.stdin.readline

    # start here
    # s,t = list(map(str,input().split()))
    string=input()

    print(atoi(string))
threading.Thread(target=main).start()