package linked_list;

class Node {
    int data;
    Node next;

    Node(int data1, Node next1, Node prev1) {
        this.data = data1;
        this.next = next1;
    }

    Node(int data1) {
        this.data = data1;
        this.next = null;
    }
}

public class Midium {
    // middle node of linked list - brute force
    public static int middleNode(Node head) {
        if (head == null)
            return 0;
        if (head.next == null)
            return head.data;

        int cnt = 0;
        Node temp = head;
        while (temp != null) {
            cnt++;
            temp = temp.next;
        }
        int mid = (cnt / 2) + 1;

        temp = head;
        int reach = 0;
        while (temp != null) {
            reach += 1;
            if (reach == mid)
                break;
            temp = temp.next;
        }
        return temp.data;
    }

    // middle node of linked list - optimal
    public static Node middleNodeOptimal(Node head) {
        Node slow = head, fast = head;

        while (fast != null && fast.next != null && slow != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }

    // reverse a singly linked list
    public static Node reverseSinglyLL(Node head) {
        if (head == null || head.next == null)
            return head;

        Node last = null, front = null;
        Node curr = head;
        while (curr != null) {
            front = curr.next;
            curr.next = last;
            last = curr;
            curr = front;
        }
        return last;
    }

    // print DLL
    public static void printLL(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }

    public static void main(String[] args) {
        Node head = new Node(2);
        head.next = new Node(3);
        head.next.next = new Node(5);
        head.next.next.next = new Node(6);
        head.next.next.next.next = new Node(10);
        head.next.next.next.next = new Node(12);
        head = reverseSinglyLL(head);
        printLL(head);

    }
}
