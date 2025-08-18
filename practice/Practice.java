package practice;

class Node {
    int data;
    Node next;

    Node(int data1, Node next1) {
        this.data = data1;
        this.next = next1;
    }
}

class Practice {
    // print LL
    public static void printLL(Node head) {
        if (head == null)
            System.out.println("");
        else {
            Node temp = head;
            while (temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
        }
    }

    // find length of LL
    public static int lengthLL(Node head) {
        int cnt = 0;
        while (head != null) {
            cnt += 1;
            head = head.next;
        }
        return cnt;
    }

    // insert a node at the head
    public static Node insertNodeLL(Node head, int val) {
        Node newNode = new Node(val, head);
        return newNode;
    }

    // search for a node
    public static String searchNode(Node head, int val) {
        while (head != null) {
            if (head.data == val)
                return "present";
            head = head.next;
        }
        return "not present";
    }

    // delete head of LL
    public static Node deleteHeadLL(Node head) {
        head = head.next;
        return head;
    }

    // delete tail of a LL
    public static Node deleteTailLL(Node head) {
        if (head == null || head.next == null) {
            return null;
        }
        Node temp = head;
        while (temp.next.next != null)
            temp = temp.next;

        temp.next = null;
        return head;
    }

    public static void main(String[] args) {
        Node head = new Node(2, null);
        head.next = new Node(3, null);
        head.next.next = new Node(4, null);

        Node temp = deleteTailLL(head);
        printLL(head);
    }
}