# check if a number or a string is palindrome 
def checkStringPalindrome(string):
    return string==string[::-1]

def checkStringPalindrome1(string):
    l,r=0,len(string)-1
    
    while l<=r:
        if string[l]!=string[r]: return False 
        l+=1
        r-=1
    return True

def checkNumPalindrome(n):
    dup=n 
    revNum=0
    while n>0:
        digit=n%10 
        revNum=(revNum*10)+digit 
        n//=10
    
    if dup==revNum: return True 
    else: return False 

def checkNumPalindrome1(n):
    lstn=",".join(str(digit) for digit in str(n))
    
    l,r=0,len(lstn)-1
    
    while l<=r:
        if lstn[l]!=lstn[r]:
            return False 
        l+=1
        r-=1
    return True 
    

string=int(input())
print(checkNumPalindrome1(string))