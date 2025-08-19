package linked_list;

import java.io.*;
import java.util.*;

// doubly linked list 
class Node {
    int data;
    Node next, prev;

    Node(int data1, Node next1, Node prev1) {
        this.data = data1;
        this.next = next1;
        this.prev = prev1;
    }

    Node(int data1) {
        this.data = data1;
        this.next = null;
        this.prev = null;
    }
}

public class DoublyLL {

    // array to DLL
    public static Node arrayToDLL(int arr[]) {
        Node head = new Node(arr[0]);
        Node prev = head;

        for (int i = 1; i < arr.length; i++) {
            Node temp = new Node(arr[i], null, prev);
            prev.next = temp;
            prev = temp;
        }
        return head;
    }

    // print DLL
    public static void printLL(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
        System.out.println();
    }

    // count number of nodes
    public static int cntNodes(Node head) {
        int cnt = 0;
        while (head != null) {
            cnt++;
            head = head.next;
        }
        return cnt;
    }

    // delete the head node
    public static Node deleteHead(Node head) {
        // no head
        if (head == null || head.next == null)
            return null;
        // more than 1 node
        Node newHead = head.next;
        newHead.prev = null;
        return newHead;
    }

    // delete tail of LL
    public static Node deleteTail(Node head) {
        if (head == null || head.next == null) {
            return null;
        }
        Node prev = head;
        Node tail = head;
        while (tail.next != null) {
            prev = tail;
            tail = tail.next;
        }
        prev.next = null;
        tail.prev = null;
        return head;
    }

    // delete kth node of LL
    public static Node deleteKthNode(Node head, int k) {
        if (head == null)
            return null;
        Node temp = head;
        int cnt = 0;

        // first reach to kth node
        while (temp != null) {
            cnt += 1;
            if (cnt == k)
                break;
            temp = temp.next;
        }
        // store prev and next element
        Node back = temp.prev;
        Node front = temp.next;
        // 3 cases

        // 1. only 1 node
        if (back == null && front == null) {
            return null;
        }
        // 2. head node
        else if (back == null) {
            return deleteHead(head);
        }
        // 3. tail node
        else if (front == null) {
            return deleteTail(head);
        } else {
            // 4. node in between
            back.next = front;
            front.prev = back;
            // detach temp
            temp.next = null;
            temp.prev = null;
        }
        return head;
    }

    // delete given node
    public static void deleteGivenNode(Node temp) {
        Node prev = temp.prev;
        Node front = temp.next;

        // front not there
        if (front == null) {
            prev.next = null;
            temp.prev = null;
            return;
        }
        // in between node
        prev.next = front;
        front.prev = prev;
        // detach temp
        temp.next = temp.prev = null;
    }

    // insert before head
    public static Node InsertBeforeHead(Node head, int val) {
        Node newHead = new Node(val, head, null);
        head.prev = newHead;
        return newHead;
    }

    // insert before tail
    public static Node InsertBeforeTail(Node head, int val) {
        if (head.next == null) {
            return InsertBeforeHead(head, val);
        }
        // reach to tail
        Node tail = head;

        while (tail.next != null) {
            tail = tail.next;
        }
        Node prev = tail.prev;
        Node newNode = new Node(val, tail, prev);
        prev.next = newNode;
        tail.prev = newNode;
        return head;
    }

    // insert before kth element
    public static Node insertBeforeKthNode(Node head, int k, int val) {
        if (k == 1)
            return InsertBeforeHead(head, val);

        Node temp = head;
        int cnt = 0;

        // reach to kth node
        while (temp != null) {
            cnt++;
            if (cnt == k)
                break;
            temp = temp.next;
        }
        Node back = temp.prev;
        Node newNode = new Node(val, temp, back);
        back.next = newNode;
        temp.prev = newNode;
        return head;

    }

    // insert before given node
    public static void insertBeforeNode(Node node, int val) {
        Node back = node.prev;
        Node newNode = new Node(val, node, back);
        back.next = newNode;
        node.prev = newNode;

    }

    // insertion after head node
    public static Node insertAfterHead(Node head, int val) {
        // no node
        if (head == null) {
            Node newNode = new Node(val, null, null);
            return newNode;
        }
        // single node
        if (head.next == null) {
            Node newNode = new Node(val, null, head);
            head.next = newNode;
            return head;
        }
        // more than 1 node
        Node front = head.next;
        Node newNode = new Node(val, front, head);
        head.next = newNode;
        front.prev = newNode;
        return head;

    }

    // insert after tail node
    public static Node insertAfterTail(Node head, int val) {
        // no head
        if (head == null) {
            return new Node(val, null, null);
        }
        // single node
        if (head.next == null) {
            Node newNode = new Node(val, null, head);
            head.next = newNode;
            return head;
        }
        // more than 1 node
        // reach to tail node
        Node tail = head;
        while (tail.next != null) {
            tail = tail.next;
        }
        Node newNode = new Node(val, null, tail);
        tail.next = newNode;
        return head;
    }

    // insertion after kth element
    public static Node insertAfterKthEle(Node head, int val, int k) {
        // no node
        if (head == null) {
            if (k == 1) {
                return new Node(val, null, null);
            } else {
                System.out.println("invalid posiitoin");
            }
        }
        // insertion after head node
        if (k == 1) {
            Node newNode = new Node(val, null, head);
            head.next = newNode;
            return head;
        }
        // in between node
        // reach to kth node
        Node temp = head;
        int cnt = 0;
        while (temp.next != null) {
            cnt += 1;
            if (cnt == k)
                break;
            temp = temp.next;
        }
        Node front = temp.next;
        // k is last node
        if (front == null) {
            Node newNode = new Node(val, null, temp);
            temp.next = newNode;
            return head;
        }
        Node newNode = new Node(val, front, temp);
        temp.next = newNode;
        front.prev = newNode;
        return head;

    }

    // insert after a given node
    public static void insertAfterNode(Node node, int val) {
        Node front = node.next;
        Node newNode = new Node(val, front, node);
        node.next = newNode;
        if (front != null) {
            front.prev = newNode;
        }
    }

    // reverse a DLL -- reverse the data
    public static void reverseDLL(Node head) {
        Node temp = head;
        Stack<Integer> stk = new Stack<>();
        // push data in stack
        while (temp != null) {
            stk.push(temp.data);
            temp = temp.next;
        }
        // pop and place in reverse
        temp = head;
        while (temp != null) {
            temp.data = stk.pop();
            temp = temp.next;
        }
    }

    // reverse a DLL - optimal single pass
    public static Node reverseDLLOptimal(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        Node curr = head;
        Node last = null;

        while (curr != null) {
            last = curr.prev;
            curr.prev = curr.next;
            curr.next = last;
            curr = curr.prev;
        }
        return last.prev;
    }

    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5 };
        Node head = arrayToDLL(arr);
        head = reverseDLLOptimal(head);
        printLL(head);
    }
}
