import sys, os

# detect if running locally (input.txt exists)
if os.path.exists("CP PRACTICE/input.txt"):
    sys.stdin = open("CP PRACTICE/input.txt", "r")
    sys.stdout = open("CP PRACTICE/output.txt", "w")


def input():
    return sys.stdin.readline().rstrip()


def solve(str):
    sum = 0
    for ele in str:
        if ele.isdigit():
            sum += int(ele)
    print(sum)


if __name__ == "__main__":
    t = int(input())
    # res = []
    for _ in range(t):
        # x, y, z = list(map(int, input().split(" ")))
        str = input()
        solve(str)
