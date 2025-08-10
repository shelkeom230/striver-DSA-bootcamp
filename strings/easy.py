import sys, threading

# reverse a sentence -- brute force 
def revSentence(sen):
    words=sen.strip().split()
    rev_words=words[::-1]
    return ' '.join(rev_words)

# largest odd number in a string -- brute force 
def largestOddNumberBrute(string):
    maxOdd="" 

    n=len(string)

    for i in range(n):
        for j in range(i,n):
            substr=string[i:j+1]

            if int(substr[-1])%2!=0:
                if maxOdd=="" or int(substr)>int(maxOdd):
                    maxOdd=substr 
    return maxOdd if maxOdd else ""

# largest odd number in a string -- better 
def largestOddNumberBetter(string):
    n=len(string)

    for i in range(n-1,-1,-1):
        if int(string[i])%2!=0:
            return string[0:i+1]
    return ""

# longest common prefix -- brute force 
def longestCmnPrefixBrute(string):
    minWord=min(string,key=len)

    for i in range(len(minWord)-1,-1,-1):
        prefix=minWord[0:i+1]
        if all(word.startswith(prefix) for word in string):
            return prefix 
    return "" 

# longest common prefix -- other approach 
def longestCommonPrefixOther(string):
    first=string[0]
    last=string[-1]

    minLength=min(len(first),len(last))

    i=0 
    while i<minLength and first[i]==last[i]:
        i+=1

    return first[:i]     

# check for isomorphic string -- brute force 
def checkIsomorphicOptimal(s,t):
    mapST,mapTS={},{}
    for c1,c2 in zip(s,t):
        if((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
            return False 
        mapST[c1]=c2
        mapTS[c2]=c1 
    return True

# rotate string brute 
def rotateStringBrute(s,t):
    n1=len(s)
    temp=""

    for i in range(n1):
        temp+=s[i+1:]+s[0:i+1]

        if temp==t:
            return True
        temp="" 
    return False 

# rotate string yet another approach 
def rotateStringOptimal(s,t):
    if t in s+t:
        return True 
    return False 

# valid anagram 
def validAnagram(s,t):
    freq_s,freq_t={},{}

    for char in s:
        freq_s[char]=freq_s.get(char,0)+1
    
    for char in t:
        freq_t[char]=freq_t.get(char,0)+1
    
    return freq_t==freq_s 

# valid anagram better approach with char array
def validAnagramBetter(s,t):
    if len(s)!=len(t):
        return False 

    count=[0]*26

    for i in range(len(s)):
        count[ord(s[i])-'a']+=1
        count[ord(t[i])-'a']-=1
    
    return all(x==0 for x in count)

def main():
    sys.stdin = open("strings/input.txt", "r")
    sys.stdout = open("strings/output.txt", "w")
    input = sys.stdin.readline

    # start here
    s,t = list(map(str,input().split()))
    print(validAnagramBetter(s,t))


threading.Thread(target=main).start()
