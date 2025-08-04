import sys, threading


# remove outer parenthesis -- brute force
def removeOuterParenthesesBrute(s):

    n = len(s)

    openCnt, closeCnt = 0, 0
    prevIndx = 0
    ans = []
    for i in range(n):
        if s[i] == "(":
            openCnt += 1
        if s[i] == ")":
            closeCnt += 1
        if openCnt == closeCnt:
            ans.append(s[prevIndx : i + 1])
            openCnt = 0
            closeCnt = 0
            prevIndx = i

    # now find the answer
    for string in ans:
        result = []
        if string.startsWith("(") and string.endsWith(")"):
            new_s = string[1:-1]
        else:
            new_s = string
        result.append(new_s)
    return result


def main():
    sys.stdin = open("binary search/input.txt", "r")
    sys.stdout = open("binary search/output.txt", "w")
    input = sys.stdin.readline

    # start here
    string = input()
    print(removeOuterParenthesesBrute(string))


threading.Thread(target=main).start()
