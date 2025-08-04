# binary search on grids
import sys, threading


def q1(n, arr):
    changes = []

    for i in range(1, n):
        val = 0
        if arr[i - 1] < arr[i]:
            val = 1
        if arr[i - 1] > arr[i]:
            val = -1

        # don't use changes[i-1], use changes[-1]
        if len(changes) == 0 or val != changes[-1]:
            changes.append(val)

    return changes == [1, -1, 1]


def q2(n, arr):
    cnt = 0

    i = 1
    while i < n:
        if arr[i] < arr[i - 1]:
            cnt += 1
            i += 2
        else:
            i += 1

    return cnt


def main():
    sys.stdin = open("practice/input.txt", "r")
    sys.stdout = open("practice/output.txt", "w")
    input = sys.stdin.readline

    # start here
    n = int(input())
    arr = list(map(int, input().split(",")))
    print(q2(n, arr))


threading.Thread(target=main).start()
