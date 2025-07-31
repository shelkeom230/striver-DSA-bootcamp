import sys, re

sys.stdout = open("basic recursion/output.txt", "w")
sys.stdin = open("basic recursion/input.txt", "r")


# print 1 infinite times
def print_one():
    print("1")
    print_one()  # recursion call


# print upto specified value
cnt = 0


def printSeq():
    global cnt
    if cnt == 3:
        return
    print(cnt)
    cnt += 1
    printSeq()


# print even numbers
even = 0


def printEven():
    global even

    if even == 10:
        print(even)
        return
    print(even)
    even += 2
    printEven()


# print odd numbers
odd = 0


def printOdd():
    global odd
    if odd == 10:
        return
    if odd % 2 != 0:
        print(odd)
    odd += 1
    printOdd()


# print your name n times
def printName1(i, n):
    # base case
    if i == n:
        print("omkar")
        return
    print("omkar")
    printName1(i + 1, n)


# print your name n times
def printName2(i, n):
    if i > n:
        return
    print("omkar")
    printName2(i + 1, n)


# print from i to n
def printInRange1(i, n):
    if i == n:
        print(i)
        return
    print(i)
    printInRange1(i + 1, n)


def printInRange2(i, n):
    if i > n:
        return
    print(i)
    printInRange2(i + 1, n)


# print even numbers from i to n
def printEvenInRange(i, n):
    if i == n + 1:
        return
    if i % 2 == 0:
        print(i)
    printEvenInRange(i + 1, n)


# print from N to 1
def printReverse1(i, n):
    if n < 1:
        return
    print(n)
    printReverse1(i, n - 1)


# print from N to 1
def printReverse2(i, n):
    # base case
    if n == i:
        print(n)
        return
    print(n)
    printReverse2(i, n - 1)


# print from 1 to N using backtracking
def printSeqBacktrack1(i, n):
    if i < 1:
        return
    printSeqBacktrack1(i - 1, n)
    print(i)


# print from N to 1 using backtracking
def printSeqBackTrack2(i, n):
    if i > n:
        return
    printSeqBackTrack2(i + 1, n)
    print(i)


# sum of first n numbers
def findSum1(i, n, s):
    if i > n:
        return s
    return findSum1(i + 1, n, s + i)


def findSum2(n, s):
    if n < 1:
        return s
    return findSum2(n - 1, s + n)


# functional way to sum first n numbers
def findSum3(n):
    if n == 0:
        return n
    return n + findSum3(n - 1)


# factorial of a number
def findFactorial(n):
    if n == 0:
        return 1
    return n * findFactorial(n - 1)


# reverse an array
def reverseArray1(a, l, r):
    if l >= r:
        return a
    a[l], a[r] = a[r], a[l]
    return reverseArray1(a, l + 1, r - 1)


# reverse an array using only 1 pointer
def reverseArray2(a, i):
    n = len(a)

    if i >= (n // 2):
        return a
    a[i], a[n - i - 1] = a[n - i - 1], a[i]
    return reverseArray2(a, i + 1)


# check string is palindrome or not
def checkPalindrome(string, i):
    string = str.lower(string)
    n = len(string)

    if i >= (n // 2):
        return True
    if string[i] != string[n - i - 1]:
        return False
    return checkPalindrome(string, i + 1)


# print fibonacci value of n
def printFib1(n):
    if n <= 1:
        return n
    return printFib1(n - 1) + printFib1(n - 2)


# print fib series upto n value
def printFibuptoN(n):
    a, b = 0, 1

    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# print n terms in fib sequence
def printnTerms(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# leetcode valid palindrome solution 1
def checkPalindromeLeetcode1(s):
    newStr = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

    if newStr == "":
        return True

    l, r = 0, len(newStr) - 1

    while l < r:
        if newStr[l] != newStr[r]:
            return False
        l += 1
        r -= 1
    return True


# leetcode check palindrome solution 2 (efficient with 0(n) time and space )
def checkPalindromeLeetcode2(s):
    newStr = ""

    for char in s:
        if char.isalnum():
            newStr += char.lower()
    return newStr == newStr[::-1]


# leetcode check palindrome solution 3 (efficient with 0(1) space and 0(n) time )
def checkAlpha(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


def checkPalindromeLeetcode3(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not checkAlpha(s[l]):
            l += 1
        while r > l and not checkAlpha(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


# find all factorials less than or equal to n
def findFactorialInRange(n):
    fact = 1
    i = 1
    result = []
    while fact <= n:
        result.append(fact)
        i += 1
        fact *= i
    return result


if __name__ == "__main__":
    n = int(input())
    # lst=list(map(int,input().split(',')))
    # string=input()

    # s=input()
    print(findFactorialInRange(n))
