import sys, threading


class Node:
    def __init__(self, data1, next1=None, prev1=None):
        self.data = data1
        self.next = next1
        self.prev = prev1


# convert from array to DLL
def arraytoLL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head


# cnt # of nodes in DLL
def cntNodesDLL(head):
    cnt = 0
    while head is not None:
        cnt += 1
        head = head.next
    return cnt


# print DLL
def printDLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def main():
    sys.stdin = open("linked list/input.txt", "r")
    sys.stdout = open("linked list/output.txt", "w")
    input = sys.stdin.readline

    # start here
    # s,t = list(map(str,input().split()))
    # string = input()

    # create a node with value 2
    arr = [1, 3, 2, 4]
    head = arraytoLL(arr)
    print(cntNodesDLL(head))


threading.Thread(target=main).start()
