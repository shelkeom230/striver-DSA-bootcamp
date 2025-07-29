# check if a number is armstrong or not 
def checkArmstrong(n):
    dup=n 
    sum=0
    
    while n>0:
        digit=n%10 
        sum+=(digit**3)
        n//=10
    
    if dup==sum: return True 
    else: return False 

# print armstrong number upto n 
def printArmstrongUptoN(n):
    for i in range(n+1):
        if checkArmstrong(i):
            print(i)
            
n=int(input())
printArmstrongUptoN(n)