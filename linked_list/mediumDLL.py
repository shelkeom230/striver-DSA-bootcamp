import sys, threading


class Node:
    def __init__(self, data1, next1=None, prev1=None):
        self.data = data1
        self.next = next1
        self.prev = prev1


# remove occurences of a node
def removeOccurencesBrute(head, x):
    if head == None:
        return head

    if head.next == None and x == head.data:
        return None

    # store values
    values = []
    temp = head

    while temp is not None:
        if temp.data != x:
            values.append(temp)
        temp = temp.next

    # built new linked list
    dummyNode = Node(-1)
    temp = dummyNode

    for i in range(len(values)):
        newNode = Node(values[i], None, temp)
        temp.next = newNode
        temp = newNode

    return dummyNode.next


# delete given node
def delete_given_node(temp):
    if temp is None:
        return

    prev = temp.prev
    front = temp.next

    # if temp is the last node
    if front is None:
        if prev:
            prev.next = None
        temp.prev = None
        return

    # if temp is in between
    if prev:
        prev.next = front
    front.prev = prev

    # detach temp
    temp.next = None
    temp.prev = None


# remove occurences of a node -- optimal
def removeOccurencesOptimal(head, x):
    if head == None:
        return head

    temp = head
    while temp is not None:
        front = temp.next  # store front before

        if temp.data == x:

            if temp == head:
                head = front

                if head:
                    head.prev = None

            # delete current node
            delete_given_node(temp)

        # go to next node
        temp = front

    return head


# find pairs with given sum in doubly linked list -- brute
def pairSumBrute(head, target):
    if head == None:
        return head

    values = []
    temp = head

    while temp is not None:
        values.append(temp.data)
        temp = temp.next

    n = len(values)

    ans = []
    freq = {}
    for i in range(n):
        freq[values[i]] = i

        req = target - values[i]
        if req in freq.values():
            ans.append((values[i], values[freq[req]]))

    return ans


# find pairs with given sum in DLL -- optimal
def findPairs(head, k):

    # Write your code here.
    # Return boolean true or false.
    # pass
    if head == None:
        return head

    ans = []
    temp = head

    while temp.next != None:
        temp = temp.next

    right = temp
    left = head

    while left.data < right.data:
        sum = left.data + right.data

        if sum == k:
            ans.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif sum > k:
            right = right.prev
        else:
            left = left.next

    return ans


# remove duplicates from sorted DLL -- brute force
def removeDupLLBrute(head):
    if head == None or head.next == None:
        return head

    temp = head
    lst = []

    while temp != None:
        if temp.data not in lst:
            lst.append(temp.data)
        temp = temp.next

    dummyNode = Node(-1)
    temp = dummyNode

    for ele in lst:
        newNode = Node(ele)
        newNode.prev = temp
        newNode.next = None
        temp.next = newNode
        temp = newNode
    return dummyNode.next


# remove duplicates from sorted DLL -- optimal
def removeDupDLLOptimal(head):
    if head == None or head.next == None:
        return head

    temp = head

    while temp.next != None:
        # duplicate found
        if temp.data == temp.next.data:
            toDelete = temp.next
            temp.next = toDelete.next
            if temp.next:
                temp.next.prev = temp
            del toDelete
        else:
            # no duplicate , go forward
            temp = temp.next
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
    head.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next = Node(8)
    # target = int(input())
    head = removeDupDLLOptimal(head)
    printLL(head)


threading.Thread(target=main).start()
