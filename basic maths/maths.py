# basic maths

import sys
import math as m

sys.stdout = open("basic maths/output.txt", "w")
sys.stdin = open("basic maths/input.txt", "r")


# reverse a number
def revNum(n):
    reverseNum = 0
    while n > 0:
        lastDigit = n % 10
        reverseNum = (reverseNum * 10) + lastDigit
        n //= 10
    return reverseNum


# check palindromic number
def checkPalindrome(n):
    if n < 0:
        print(f"{n} is not palindrome")
        return
    original = n
    revNum = 0
    while n > 0:
        digit = n % 10
        revNum = (revNum * 10) + digit
        n //= 10

    if revNum == original:
        print(f"{original} is palindrome")
    else:
        print(f"{original} is not palindrome")


# count digits
def cntDigits1(n):
    cnt = 0
    while n > 0:
        digit = n % 10
        cnt += 1
        n //= 10
    return cnt


# print digits of a number
def cntDigits2(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n //= 10


# use log to count digits
def cntDigits3(n):
    # use logarithm
    digits = (int)(m.log10(n)) + 1
    return digits


# check armstrong number
def checkArmstrong(n):
    if n < 0:
        return False
    else:
        dup = n
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit**3
            n //= 10
        if dup == sum:
            return True
        else:
            return False


# print armstrong upto n
def printArmstrong(n):
    for i in range(1, n):
        if checkArmstrong(i):
            print(i)


# print all divisors
def printDivisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


# optimised way to print divisors
def printDivisors2(n):
    factors = []
    for i in range(1, (int)(m.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if (n // i) != i:
                factors.append(n // i)
    factors = sorted(factors)
    for ele in factors:
        print(ele)


# check prime number
def checkPrime1(n):
    cnt = 0
    # brute force approach
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


def checkPrime2(n):
    if n < 2:
        return False
    else:
        for i in range(2, (int)(m.sqrt(n) + 1)):
            if n % i == 0:
                return False
    return True


# check prime optimised approach
def checkPrime3(n):
    cnt = 0
    for i in range(1, (int)(m.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            if (n // i) != i:
                cnt += 1
    if cnt == 2:
        return True
    else:
        return False


# find GCD or HCF
def findGCD1(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2)):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    print(gcd)


# GCD quite better way
def findGCD2(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            print(i)
            break


# GCD using euclidien method 0(log(phi)min(n1,n2))
def findGCD3(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1

    if n1 == 0:
        return n2
    return n1


# find gcd and lcm very efficiently
def findgcdlcm(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    gcd = a
    lcm = int(a * b) / gcd
    return [gcd, lcm]


if __name__ == "__main__":
    # n=int(input())
    n1 = int(input())
    n2 = int(input())
    print(findgcdlcm(n1, n2))
