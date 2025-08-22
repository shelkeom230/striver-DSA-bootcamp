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
        Node head = new Node(2);
        head.next = new Node(3);
        head.next.next = new Node(5);
        head.next.next.next = new Node(6);
        head.next = head;
        Node temp = detectStartingPointOptimal(head);
        out.println(temp.data);
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
        public V value;

        public Pair() {
        }

        public Pair(K k, V v) {
            key = k;
            value = v;
        }

        public String toString() {
            return "(" + key + ", " + value + ")";
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

        // Print a single value
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

        // Print a value with a newline
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