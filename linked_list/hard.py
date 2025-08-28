import sys, threading


class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def reverseSinglyLL(head):
    if head is None or head.next is None:
        return head

    last = None
    curr = head

    while curr is not None:
        front = curr.next  # store next node
        curr.next = last  # reverse the link
        last = curr  # move last forward
        curr = front  # move curr forward


def reverse(arr, start, end):
    left, right = start, end - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# reverse linked list in groups of size k
def revLL(head, k):
    if head == None or head.next == None:
        return head

    values = []
    temp = head

    while temp is not None:
        values.append(temp.data)
        temp = temp.next

    cnt = len(values) // k

    for i in range(cnt):
        reverse(values, i * k, i * k + k)

    # now copy back values
    temp = head
    for ele in values:
        temp.data = ele
        temp = temp.next
    return head


# reverse LL into k groups -- optimal
def getKthNode(temp, k):
    k -= 1
    while temp != None and k > 0:
        k -= 1
        temp = temp.next
    return temp


def revLLOptimal(head, k):
    temp = head
    prevLast = None

    while temp is not None:
        kthNode = getKthNode(temp, k)

        if kthNode == None:
            if prevLast:
                prevLast.next = temp
                break

        nextNode = kthNode.next
        kthNode.next = None
        reverseSinglyLL(temp)

        if temp == head:
            head = kthNode
        else:
            prevLast.next = kthNode

        prevLast = temp
        temp = nextNode

    return head


# print LL
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def main():
    sys.stdin = open("linked_list/input.txt", "r")
    sys.stdout = open("linked_list/output.txt", "w")
    input = sys.stdin.readline

    # start here
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next.next.next = Node(10)
    k = int(input())
    head = revLLOptimal(head, k)
    printLL(head)


threading.Thread(target=main).start()
