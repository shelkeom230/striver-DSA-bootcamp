def sumDigits(n):
    totalsum=0
    while n>0:
        digit=n%10 
        totalsum+=digit 
        n//=10
    return totalsum

n=int(input())
print(sumDigits(n))