# basics of linked list
import sys, threading


# creating a linked list Node
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


# traverse the LL
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


# find length of LL
def lengthLL(head):
    cnt = 0
    while head is not None:
        cnt += 1
        head = head.next
    return cnt


# insert a new node at the head
def insertNodeLL(head, val):
    newNode = Node(val, head)
    return newNode


# search a node
def searchNode(head, val):
    while head is not None:
        if head.data == val:
            return "present"
        head = head.next
    return "not present"


# delete head of LL
def deleteHeadLL(head):
    head = head.next
    return head


# delete tail of a LL
def deleteTailLL(head):
    if head == None or head.next == None:
        return None

    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head


# delete kth node of a linked list
def deleteKthNodeLL(head, k):
    if head == None:
        return head

    if k == 1:
        head = head.next
        return head

    cnt = 0
    temp = head
    prev = None

    while temp is not None:
        cnt += 1

        if cnt == k:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head


# delete  node of a linked list by value
def deleteNodeByValLL(head, ele):
    if head == None:
        return head

    if head.data == ele:
        head = head.next
        return head

    temp = head
    prev = None

    while temp is not None:

        if temp.data == ele:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head


# insert a node at start of LL
def insertAtHeadLL(head, val):
    newNode = Node(val, head)
    return newNode


# insert a node at end of LL
def insertAtTailLL(head, val):
    if head == None:
        return Node(val, None)

    temp = head
    while temp.next is not None:
        temp = temp.next

    newNode = Node(val, None)
    temp.next = newNode
    return head


# insert at given position k
def insertAtPosKLL(head, val, k):
    if head == None:
        if k == 1:
            return Node(val, head)
        else:
            # invalid k value when head is null
            return None

    # k >1
    # find the previous node
    cnt = 0
    temp = head
    while temp != None:
        cnt += 1
        if cnt == k - 1:
            break
        temp = temp.next
    newNode = Node(val, None)
    newNode.next = temp.next
    temp.next = newNode
    return head


# insert before given value x
def insertBeforeXLL(head, val, x):
    if head == None:
        return head

    if head.data == x:
        return Node(val, head)

    temp = head

    while temp.next.data != x:
        temp = temp.next
    newNode = Node(val, None)
    newNode.next = temp.next
    temp.next = newNode
    return head


def main():
    sys.stdin = open("linked list/input.txt", "r")
    sys.stdout = open("linked list/output.txt", "w")
    input = sys.stdin.readline

    # start here
    # s,t = list(map(str,input().split()))
    # string = input()

    # create a node with value 2
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(6)

    head = insertAtHeadLL(head, 10)
    printLL(head)


threading.Thread(target=main).start()
