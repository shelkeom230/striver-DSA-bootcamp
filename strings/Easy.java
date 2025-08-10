package strings;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

// strings easy problems 
public class Easy {
     static FastReader in;
    static FastWriter out;

       // reverse a sentence -- brute force
    public static String revSentence(String sen) {
        String[] words = sen.trim().split("\\s+"); // split by spaces
        Collections.reverse(Arrays.asList(words));
        return String.join(" ", words);
    }

    // largest odd number in a string -- brute force
    public static String largestOddNumberBrute(String str) {
        String maxOdd = "";
        int n = str.length();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String substr = str.substring(i, j + 1);
                if ((substr.charAt(substr.length() - 1) - '0') % 2 != 0) {
                    if (maxOdd.equals("") || Integer.parseInt(substr) > Integer.parseInt(maxOdd)) {
                        maxOdd = substr;
                    }
                }
            }
        }
        return maxOdd.equals("") ? "" : maxOdd;
    }

    // largest odd number in a string -- better
    public static String largestOddNumberBetter(String str) {
        int n = str.length();
        for (int i = n - 1; i >= 0; i--) {
            if ((str.charAt(i) - '0') % 2 != 0) {
                return str.substring(0, i + 1);
            }
        }
        return "";
    }

    // longest common prefix -- brute force
    public static String longestCmnPrefixBrute(String[] arr) {
        String minWord = Arrays.stream(arr).min(Comparator.comparingInt(String::length)).orElse("");
        for (int i = minWord.length() - 1; i >= 0; i--) {
            String prefix = minWord.substring(0, i + 1);
            boolean allMatch = true;
            for (String word : arr) {
                if (!word.startsWith(prefix)) {
                    allMatch = false;
                    break;
                }
            }
            if (allMatch) return prefix;
        }
        return "";
    }

    // longest common prefix -- other approach
    public static String longestCommonPrefixOther(String[] arr) {
        String first = arr[0];
        String last = arr[arr.length - 1];
        int minLength = Math.min(first.length(), last.length());

        int i = 0;
        while (i < minLength && first.charAt(i) == last.charAt(i)) {
            i++;
        }
        return first.substring(0, i);
    }

    // check for isomorphic string -- optimal
    public static boolean checkIsomorphicOptimal(String s, String t) {
        Map<Character, Character> mapST = new HashMap<>();
        Map<Character, Character> mapTS = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i), c2 = t.charAt(i);
            if ((mapST.containsKey(c1) && mapST.get(c1) != c2) ||
                (mapTS.containsKey(c2) && mapTS.get(c2) != c1)) {
                return false;
            }
            mapST.put(c1, c2);
            mapTS.put(c2, c1);
        }
        return true;
    }

    // rotate string brute
    public static boolean rotateStringBrute(String s, String t) {
        int n1 = s.length();
        String temp = "";
        for (int i = 0; i < n1; i++) {
            temp += s.substring(i + 1) + s.substring(0, i + 1);
            if (temp.equals(t)) {
                return true;
            }
            temp = "";
        }
        return false;
    }

    // rotate string -- optimal
    public static boolean rotateStringOptimal(String s, String t) {
        return (s + s).contains(t);
    }

    // valid anagram
    public static boolean validAnagram(String s, String t) {
        Map<Character, Integer> freqS = new HashMap<>();
        Map<Character, Integer> freqT = new HashMap<>();

        for (char c : s.toCharArray()) {
            freqS.put(c, freqS.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            freqT.put(c, freqT.getOrDefault(c, 0) + 1);
        }
        return freqS.equals(freqT);
    }

    // valid anagram -- better approach with array
    public static boolean validAnagramBetter(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int val : count) {
            if (val != 0) return false;
        }
        return true;
    }
    
    public static void main(String[] args) throws Exception {
        // For local testing: read from input.txt and write to output.txt
        in = new FastReader("strings/input.txt");
        out = new FastWriter("strings/output.txt");

        // take input from here
       
    }

    // ------------------ FAST READER ------------------
    static class FastReader {
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        private final InputStream in;

        FastReader(String fileName) throws FileNotFoundException {
            in = new FileInputStream(fileName);
        }

        private int readByte() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len == -1) return -1;
            }
            return buffer[ptr++];
        }

        String next() throws IOException {
            int c;
            while ((c = readByte()) != -1 && c <= ' '); // skip whitespace
            StringBuilder sb = new StringBuilder();
            while (c != -1 && c > ' ') {
                sb.append((char) c);
                c = readByte();
            }
            return sb.toString();
        }

        int nextInt() throws IOException {
            return (int) nextLong();
        }

        long nextLong() throws IOException {
            int c;
            while ((c = readByte()) != -1 && c <= ' ');
            boolean neg = (c == '-');
            if (neg) c = readByte();
            long val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = readByte();
            }
            return neg ? -val : val;
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }
    }

    // ------------------ FAST WRITER ------------------
    static class FastWriter {
        private final BufferedWriter bw;

        FastWriter(String fileName) throws IOException {
            bw = new BufferedWriter(new FileWriter(fileName));
        }

        void print(Object obj) throws IOException {
            bw.write(String.valueOf(obj));
        }

        void println(Object obj) throws IOException {
            bw.write(String.valueOf(obj));
            bw.newLine();
        }

        void close() throws IOException {
            bw.flush();
            bw.close();
        }
    }
}
