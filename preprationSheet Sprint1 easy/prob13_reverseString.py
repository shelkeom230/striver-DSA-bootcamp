# reverse a string 
def revString(string):
    return string[::-1].replace(' ','')

# quite good approach 2 pointers 
def revString2(string):
    l,r=0,len(string)-1
    string=list(string)
    
    while l<=r:
        string[l],string[r]=string[r],string[l]
        l+=1
        r-=1
    return ''.join(string).replace(' ','')

string=input()
print(revString2(string))