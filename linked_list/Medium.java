package linked_list;

import java.io.*;
import java.util.*;
import java.math.*;

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

public class Medium {

    // your functions here.
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

    // reverse a singly linked list -- brute force
    public static Node reverseSinglyLLBrute(Node head) {
        if (head == null || head.next == null)
            return head;

        Node temp = head;
        Stack<Integer> stack = new Stack<>();
        while (temp != null) {
            stack.push(temp.data);
            temp = temp.next;
        }
        temp = head;
        while (temp != null) {
            temp.data = stack.pop();
            temp = temp.next;
        }
        return head;
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

    // reverse a singly linked list -- recursive version
    public static Node reverseSinglyLLRecursion(Node head) {
        if (head == null || head.next == null)
            return head;

        Node newHead = reverseSinglyLLRecursion(head.next);
        Node front = head.next;
        front.next = head;
        head.next = null;
        return newHead;
    }

    // detect cycle in a linked list -- brute force
    public static boolean detectCycleBrute(Node head) {
        if (head == null || head.next == null)
            return false;
        Node temp = head;
        Map<Node, Integer> nodeMap = new HashMap<>();
        while (temp != null) {
            if (nodeMap.containsKey(temp))
                return true;

            nodeMap.put(temp, 1);
            temp = temp.next;
        }
        return false;
    }

    // detect cycle in a linked list -- optimal
    public static boolean detectCycleOptimal(Node head) {
        if (head == null || head.next == null)
            return false;

        Node fast = head, slow = head;

        while (fast != null && fast.next != null && slow != null) {
            fast = fast.next.next;
            if (slow == fast)
                return true;
            slow = slow.next;
        }
        return false;
    }

    // detect starting point of loop in LL - brute force
    public static Node detectStartingPointBrute(Node head) {
        if (head == null || head.next == null) {
            return null;
        }

        Node temp = head;
        Map<Node, Integer> nodeMap = new HashMap<>();
        int nodeCnt = 0;

        while (temp != null) {
            if (nodeMap.containsKey(temp)) {
                return temp;
            }

            nodeMap.put(temp, nodeCnt);
            nodeCnt++;
            temp = temp.next;
        }

        return null;
    }

    // detect starting point of loop in LL - optimal
    public static Node detectStartingPointOptimal(Node head) {
        if (head == null || head.next == null) {
            return null;
        }

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                // loop detected
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null;
    }

    // length of loop in LL -- brute force
    public static int lengthOfLoopBrute(Node head) {
        if (head == null) {
            return 0;
        }
        if (head.next == null) {
            return 1;
        }

        int cnt = 0;
        Map<Node, Integer> nodeMap = new HashMap<>();
        Node temp = head;

        while (temp != null) {
            if (nodeMap.containsKey(temp)) {
                return cnt - nodeMap.get(temp);
            }

            nodeMap.put(temp, cnt);
            cnt++;
            temp = temp.next;
        }
        return 0;
    }

    // length of loop in LL -- optimal
    public static int lengthOfLoopOptimal(Node head) {
        if (head == null || head.next == null) {
            return 0;
        }

        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                // loop detected
                int cnt = 1;
                fast = fast.next;

                // find the length of loop
                while (fast != slow) {
                    fast = fast.next;
                    cnt++;
                }
                return cnt;
            }
        }
        return 0;
    }

    // check for palindrome LL
    public static boolean checkPalindromeBrute(Node head) {
        if (head == null || head.next == null)
            return true;

        Node curr = head;
        Stack<Integer> stack = new Stack<>();
        while (curr != null) {
            stack.push(curr.data);
            curr = curr.next;
        }

        curr = head;
        while (curr != null) {
            if (curr.data != stack.pop())
                return false;
            curr = curr.next;
        }
        return true;
    }

    public static boolean isPalindromeOptimal(Node head) {
        if (head == null || head.next == null)
            return true;
        Node slow = head, fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        Node newHead = reverseSinglyLL(slow.next);
        Node first = head;
        Node second = newHead;
        while (second != null) {
            if (first.data != second.data) {
                reverseSinglyLL(newHead);
                return false;
            }
            ;
            first = first.next;
            second = second.next;
        }
        reverseSinglyLL(newHead);
        return true;

    }

    // segrate even and odd nodes in LL -- brute 1
    public static Node segregateEvenOddNodesBrute(Node head) {
        if (head == null || head.next == null)
            return head;

        ArrayList<Integer> even = new ArrayList<>();
        ArrayList<Integer> odd = new ArrayList<>();

        // seprate even and odd dataues
        Node curr = head;
        int cnt = 1;
        while (curr != null) {
            if (cnt % 2 == 0) {
                even.add(curr.data);
                cnt += 1;
                curr = curr.next;
            } else {
                odd.add(curr.data);
                cnt += 1;
                curr = curr.next;
            }
        }

        // put even dataues first
        int i = 0;
        curr = head;
        while (i < even.size()) {
            curr.data = even.get(i);
            i++;
            curr = curr.next;
        }

        // put odd dataues
        int j = 0;
        while (j < odd.size()) {
            curr.data = odd.get(j);
            j++;
            curr = curr.next;
        }
        return head;
    }

    // segrate even and odd nodes in LL -- brute 2 another good approach
    public static Node segregateEvenOddNodesBrute2(Node head) {
        if (head == null || head.next == null)
            return head;

        ArrayList<Integer> list = new ArrayList<>();

        Node curr = head;
        // put odd nodes first
        while (curr != null && curr.next != null) {
            list.add(curr.data);
            curr = curr.next.next;
        }
        // put last odd node
        if (curr != null)
            list.add(curr.data);

        // put even nodes first
        curr = head.next;
        while (curr != null && curr.next != null) {
            list.add(curr.data);
            curr = curr.next.next;
        }
        if (curr != null)
            list.add(curr.data);

        // put back dataues to LL
        int i = 0;
        curr = head;
        while (curr != null) {
            i++;
            curr.data = list.get(i);
            curr = curr.next;
        }
        return head;
    }

    // segrate even and odd nodes in LL --optimal approach
    public static Node oddEvenListOptimal(Node head) {
        if (head == null || head.next == null)
            return head;

        Node odd = head;
        Node even = head.next;
        Node evenHead = head.next;

        while (even != null && even.next != null) {
            odd.next = odd.next.next;
            even.next = even.next.next;

            odd = odd.next;
            even = even.next;
        }
        odd.next = evenHead;
        return head;
    }

    // remove nth node from end of LL -- extreme brute force with extra space as
    // weell
    public static Node removeNthNodeBrute(Node head, int n) {
        if (head.next == null && n == 1)
            return null;

        ArrayList<Integer> list = new ArrayList<>();

        Node curr = head;
        while (curr != null) {
            list.add(curr.data);
            curr = curr.next;
        }
        // calculate for 1 based index
        int deleteIndex = list.size() - n + 1;

        if (deleteIndex == 1) {
            // remove head
            Node newHead = head.next;
            // detach current head
            head.next = null;
            return newHead;
        }
        int cnt = 0;
        curr = head;
        Node back = null;
        while (curr != null) {
            cnt++;
            if (cnt == deleteIndex) {
                // delete that node
                back.next = curr.next;
                curr.next = null;
                break;
            }
            back = curr;
            curr = curr.next;
        }
        return head;
    }

    // remove nth node from end of LL -- brute force without extra space
    public static Node removeNthNodeBrute2(Node head, int n) {
        int cnt = 0;
        Node curr = head;
        while (curr != null) {
            cnt++;
            curr = curr.next;
        }

        if (cnt == n) {
            // removing head
            Node newHead = head.next;
            head.next = null;
            return newHead;
        }

        int res = cnt - n;
        curr = head;
        while (curr != null) {
            res--;

            if (res == 0) {
                Node deleteNode = curr.next;
                curr.next = curr.next.next;
                deleteNode.next = null;
                break;
            }
            curr = curr.next;
        }
        return head;
    }

    // remove nth node from the end of LL -- optimal
    public static Node removeNthFromEndOptimal(Node head, int n) {
        // optimal
        // move fast pointer n steps ahead
        Node fast = head;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }
        // if fast is at last node, i.e n=length of list, delete head node
        if (fast == null)
            return head.next;
        Node slow = head;

        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        Node deleteNode = slow.next;
        slow.next = slow.next.next;
        deleteNode.next = null;
        return head;

    }

    // remove middle node of a linked list -- brute force
    public static Node deleteMiddleBrute(Node head) {
        if (head.next == null)
            return null;

        int cnt = 0;
        // count total nodes
        Node curr = head;
        while (curr != null) {
            cnt++;
            curr = curr.next;
        }

        // find middle position
        int mid = (cnt / 2) + 1;
        curr = head;
        int reached = 0;

        while (curr != null) {
            reached++;
            if (reached == mid - 1) {
                curr.next = curr.next.next;
                break;
            }
            curr = curr.next;
        }
        return head;

    }

    // sort linnked list - brute force
    public static Node sortListBrute(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        ArrayList<Integer> list = new ArrayList<>();
        Node curr = head;

        while (curr != null) {
            list.add(curr.data);
            curr = curr.next;
        }
        int i = 0;
        curr = head;
        while (curr != null) {
            curr.data = list.get(i);
            i++;
            curr = curr.next;
        }
        return head;
    }

    // find middle node of LL
    public Node findMiddle(Node head) {
        // slightly changed tortoise and hare algorithm
        Node slow = head;
        Node fast = head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    // sort linked list -- optimal
    public Node merge(Node list1, Node list2) {
        Node dummyNode = new Node(-1);
        Node temp = dummyNode;
        while (list1 != null && list2 != null) {
            if (list1.data < list2.data) {
                temp.next = list1;
                temp = list1;
                list1 = list1.next;
            } else {
                temp.next = list2;
                temp = list2;
                list2 = list2.next;
            }
        }
        if (list1 != null)
            temp.next = list1;
        else
            temp.next = list2;
        return dummyNode.next;
    }

    // sort linked list -- optimal
    public Node sortListOptimal(Node head) {
        if (head == null || head.next == null)
            return head;
        Node middle = findMiddle(head);
        Node leftHead = head, rightHead = middle.next;
        middle.next = null;
        leftHead = sortListOptimal(leftHead);
        rightHead = sortListOptimal(rightHead);
        return merge(leftHead, rightHead);

    }

    // sort a LL of 0,1 and 2's -- brute 1 most inefficient
    public static Node sortListBrute1(Node head) {
        if (head == null || head.next == null)
            return head;

        List<Integer> list = new ArrayList<>();
        Node curr = head;
        while (curr != null) {
            list.add(curr.data);
            curr = curr.next;
        }

        Collections.sort(list);

        // copy back again
        curr = head;
        int i = 0;
        while (curr != null) {
            curr.data = list.get(i);
            i++;
            curr = curr.next;
        }
        return head;
    }

    // sort a LL of 0,1 and 2's -- brute 2 without extra space
    public static Node sortListBrute2(Node head) {
        if (head == null || head.next == null)
            return head;

        int cnt0 = 0, cnt1 = 0, cnt2 = 0;

        Node curr = head;

        while (curr != null) {
            if (curr.data == 0)
                cnt0++;
            else if (curr.data == 1)
                cnt1++;
            else
                cnt2++;
            curr = curr.next;
        }

        // copy back values
        curr = head;
        while (curr != null) {
            if (cnt0 > 0) {
                curr.data = 0;
                cnt0--;
            } else if (cnt1 > 0) {
                curr.data = 1;
                cnt1--;
            } else {
                curr.data = 2;
                cnt2--;
            }
            curr = curr.next;
        }
        return head;
    }

    // sort a LL of 0,1 and 2's -- optimal
    public static Node sortList(Node head) {
        // Write your code here
        if (head == null || head.next == null)
            return head;

        Node zeroHead = new Node(-1);
        Node oneHead = new Node(-1);
        Node twoHead = new Node(-1);

        Node zero = zeroHead;
        Node one = oneHead;
        Node two = twoHead;

        Node curr = head;

        while (curr != null) {
            if (curr.data == 0) {
                zero.next = curr;
                zero = curr;
            } else if (curr.data == 1) {
                one.next = curr;
                one = curr;
            } else {
                two.next = curr;
                two = curr;
            }
            curr = curr.next;
        }

        // link changes
        zero.next = (oneHead.next != null) ? oneHead.next : twoHead.next;
        one.next = (twoHead.next != null) ? twoHead.next : null;
        two.next = null;
        return zeroHead.next;
    }

    // intersection of 2 LL -- brute force
    public static Node intersectionLLBrute(Node headA, Node headB) {

        Node temp = headA;
        Map<Node, Integer> mpp = new HashMap<>();

        while (temp != null) {
            mpp.put(temp, 1);
            temp = temp.next;
        }

        // search exact similar node in second LL now
        temp = headB;
        while (temp != null) {
            if (mpp.containsKey(temp))
                return temp;
            temp = temp.next;
        }
        return null;
    }

    // intersection of 2 LL -- better solution
    public static int findIntersectionBetter(Node firstHead, Node secondHead) {
        // Write your code here
        Node temp = firstHead;
        int cnt1 = 0, cnt2 = 0;

        while (temp != null) {
            cnt1++;
            temp = temp.next;
        }

        temp = secondHead;
        while (temp != null) {
            cnt2++;
            temp = temp.next;
        }

        // find the diff
        int diff = Integer.MIN_VALUE;
        Node temp2 = new Node(-1);

        if (cnt1 > cnt2) {
            diff = cnt1 - cnt2;
            temp = firstHead;
            for (int i = 0; i < diff; i++) {
                temp = temp.next;
            }
            temp2 = secondHead;
        } else {
            diff = cnt2 - cnt1;
            temp = secondHead;
            for (int i = 0; i < diff; i++) {
                temp = temp.next;
            }
            temp2 = firstHead;
        }

        // find the answer
        while (temp != null && temp2 != null) {
            if (temp == temp2)
                return temp.data;
            temp = temp.next;
            temp2 = temp2.next;
        }
        return -1;
    }

    // get intersection node -- optimal
    public Node getIntersectionNodeOptimal(Node headA, Node headB) {
        Node temp1 = headA, temp2 = headB;

        while (temp1 != null || temp2 != null) {
            if (temp1 == temp2)
                return temp1;
            else if (temp1 == null)
                temp1 = headB;
            else if (temp2 == null)
                temp2 = headA;
            else {
                temp1 = temp1.next;
                temp2 = temp2.next;
            }
        }
        return null;

    }

    // add 1 to a LL number -- extreme brute force
    public static Node addOneBrute(Node head) {
        if (head == null)
            return null;

        head = reverseSinglyLL(head);
        Node temp = head;
        int carry = 1;

        while (temp != null) {
            temp.data += carry;

            if (temp.data < 10) {
                carry = 0;
                break;
            } else {
                temp.data = 0;
                carry = 1;

            }
            temp = temp.next;
        }

        // get the result
        if (carry == 1) {
            Node newHead = new Node(1);
            // reverse again
            head = reverseSinglyLL(head);
            newHead.next = head;
            return newHead;
        }
        // simply return by reversing
        return reverseSinglyLL(head);

    }

    public static int helper(Node temp) {
        if (temp == null)
            return 1;

        int carry = helper(temp.next);

        // backtracking code
        temp.data += carry;

        if (temp.data < 10) {
            return 0;
        }
        temp.data = 0;
        return 1;
    }

    public static Node addOne(Node head) {
        // Write your code here.
        int carry = helper(head);

        if (carry == 1) {
            Node newHead = new Node(1);
            newHead.next = head;
            return newHead;
        }
        return head;
    }

    // add 2 number represented by LL
    public static Node add2NumbersLL(Node l1, Node l2) {
        Node t1 = l1, t2 = l2, dummyNode = new Node(-1);
        Node curr = dummyNode;
        int carry = 0, sum = 0;

        while (t1 != null || t2 != null) {
            sum = carry;
            if (t1 != null)
                sum += t1.data;
            if (t2 != null)
                sum += t2.data;

            Node newNode = new Node(sum % 10);
            carry = sum / 10;

            curr.next = newNode;
            curr = newNode;

            if (t1 != null)
                t1 = t1.next;
            if (t2 != null)
                t2 = t2.next;
        }

        if (carry == 1) {
            Node newNode = new Node(carry);
            curr.next = newNode;
        }
        return dummyNode.next;

    }

    // print DLL
    public static void printLL(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }

    public static void main(String[] args) throws Exception {

        // int t = 1;
        // t = in.nextInt();
        // while (t != 0) {
        // solve();
        // t--;
        // }
        Node head = new Node(1);
        head.next = new Node(9);
        head.next.next = new Node(9);

        Node head2 = new Node(2);
        head2.next = new Node(3);
        head2.next.next = new Node(3);
        head = add2NumbersLL(head, head2);
        printLL(head);

        out.close();
    }

    static FastReader in = new FastReader();
    static FastWriter out = new FastWriter();

    static void debug(Object... argObjects) throws IOException {
        out.println(Arrays.deepToString(argObjects));
    }

    static final int MOD = (int) (1e9 + 7);
    static final int MAXI = Integer.MAX_VALUE;
    static final int MINI = Integer.MIN_VALUE;
    static final long MAXL = Long.MAX_VALUE;
    static final long MINL = Long.MIN_VALUE;
    static final double MAXD = Double.MAX_VALUE;
    static final double MIND = Double.MIN_VALUE;
    static final float MINF = Float.MIN_VALUE;
    static final float MAXF = Float.MAX_VALUE;

    static class Pair<K, V> {
        public K key;
        public V dataue;

        public Pair() {
        }

        public Pair(K k, V v) {
            key = k;
            dataue = v;
        }

        public String toString() {
            return "(" + key + ", " + dataue + ")";
        }
    }

    static class Triplet<F, S, T> {
        public F first;
        public S second;
        public T third;

        public Triplet() {
        }

        public Triplet(F f, S s, T t) {
            first = f;
            second = s;
            third = t;
        }

        public String toString() {
            return "(" + first + ", " + second + ", " + third + ")";
        }
    }

    static class FastReader {

        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static class FastWriter {
        private final BufferedWriter bw;

        public FastWriter() {
            bw = new BufferedWriter(new OutputStreamWriter(System.out), 1 << 16);
        }

        // Print a single dataue
        public void print(String s) throws IOException {
            bw.write(s);
        }

        public void print(int x) throws IOException {
            bw.write(Integer.toString(x));
        }

        public void print(long x) throws IOException {
            bw.write(Long.toString(x));
        }

        public void print(double x) throws IOException {
            bw.write(Double.toString(x));
        }

        public void print(Object obj) throws IOException {
            bw.write(obj.toString());
        }

        // Print a dataue with a newline
        public void println(String s) throws IOException {
            bw.write(s);
            bw.newLine();
        }

        public void println(int x) throws IOException {
            bw.write(Integer.toString(x));
            bw.newLine();
        }

        public void println(long x) throws IOException {
            bw.write(Long.toString(x));
            bw.newLine();
        }

        public void println(double x) throws IOException {
            bw.write(Double.toString(x));
            bw.newLine();
        }

        public void println(Object obj) throws IOException {
            bw.write(obj.toString());
            bw.newLine();
        }

        // Print arrays
        public void printArray(int[] arr) throws IOException {
            for (int x : arr) {
                print(x + " ");
            }
            println("");
        }

        public void printArray(long[] arr) throws IOException {
            for (long x : arr) {
                print(x + " ");
            }
            println("");
        }

        public void printArray(double[] arr) throws IOException {
            for (double x : arr) {
                print(x + " ");
            }
            println("");
        }

        // Print collections
        public <T> void printCollection(Collection<T> col) throws IOException {
            for (T x : col) {
                print(x.toString() + " ");
            }
            println("");
        }

        // Flush the buffer
        public void flush() throws IOException {
            bw.flush();
        }

        // Close the writer
        public void close() throws IOException {
            bw.close();
        }
    }

}