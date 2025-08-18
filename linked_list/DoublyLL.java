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
            return deleteHeadDLL(head);
        }
        // 3. tail node
        else if (front == null) {
            return deleteTailLL(head);
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

    public static void main(String[] args) {
        int arr[] = { 1, 3, 2, 4, 5 };
        Node head = arrayToDLL(arr);
        insertBeforeNode(head.next.next.next.next, 100);
        printLL(head);
    }
}