import sys, threading


# linked list midium problems
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


# find middle node of a linked list - brute force
def findMiddleBrute(head):
    if head == None or head.next == None:
        return head
    cnt = 0
    temp = head
    while temp is not None:
        cnt += 1
        temp = temp.next

    reached = 0
    mid = (cnt // 2) + 1
    temp = head

    while temp is not None:
        reached += 1
        if reached == mid:
            break
        temp = temp.next
    return temp.data


# find middle node of a linked list - optimal
def findMiddleOptimal(head):
    if head == None or head.next == None:
        return head

    fast, slow = head, head
    while fast != None and fast.next != None and slow != None:
        fast = fast.next.next
        slow = slow.next
    return slow.data


# reverse a singly linked list -- brute force
def reverse_singly_ll_brute(head):
    if head is None or head.next is None:
        return head

    temp = head
    stack = []
    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next

    return head


# reverse a singly linked list -- iterative optimal
def reverse_singly_ll(head):
    if head is None or head.next is None:
        return head

    last = None
    curr = head
    while curr:
        front = curr.next
        curr.next = last
        last = curr
        curr = front

    return last


# reverse a singly linked list -- recursive version
def reverse_singly_ll_recursion(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_singly_ll_recursion(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head


# detect cycle in a linked list -- brute force
def detect_cycle_brute(head):
    if head is None or head.next is None:
        return False

    temp = head
    node_map = set()
    while temp:
        if temp in node_map:
            return True
        node_map.add(temp)
        temp = temp.next

    return False


# detect cycle in a linked list -- optimal (Floyd’s Cycle Detection)
def detect_cycle_optimal(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        if slow == fast:
            return True
        slow = slow.next

    return False


# detect starting point of loop in LL - brute force
def detectStartingPointBrute(head):
    if head == None or head.next == None:
        return None

    temp = head
    nodeMap = {}
    nodeCnt = -1
    while temp != None:
        if temp in nodeMap:
            return nodeCnt

        nodeMap[temp] = 1
        nodeCnt += 1
        temp = temp.next

    return None


# detect starting point of loop in LL - optimal
def detectStartingPointOptimal(head):
    slow, fast = head, head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # loop detected
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


# length of loop in LL -- brute force
def lengthOfLoop(head):
    if head == None:
        return 0
    if head.next == None:
        return 1

    cnt = 0
    nodeMap = {}
    temp = head
    while temp != None:
        cnt += 1
        if temp in nodeMap:
            cnt += 1
            return cnt - nodeMap[temp]

        nodeMap[temp] = cnt
        temp = temp.next
    return 0


# length of loop in LL -- optimal
def lengthOfLoopOptimal(head):

    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # loop detected
            cnt = 1
            fast = fast.next

            # find the length of loop
            while fast != slow:
                fast = fast.next
                cnt += 1
            return cnt
    return 0


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
    head.next.next.next = head.next
    length = lengthOfLoopOptimal(head)
    print(length)


threading.Thread(target=main).start()
