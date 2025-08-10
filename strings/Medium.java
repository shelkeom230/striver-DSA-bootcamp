package strings;
import java.util.*;

public class Medium {

    // sort string by freq of chars - O(k log k)
    public static String sortString(String str) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : str.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        // sort by frequency in descending order
        List<Map.Entry<Character, Integer>> list = new ArrayList<>(freq.entrySet());
        list.sort((a, b) -> b.getValue() - a.getValue());

        StringBuilder res = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : list) {
            char c = entry.getKey();
            if (c != ' ') {
                res.append(String.valueOf(c).repeat(entry.getValue()));
            }
        }
        return res.toString();
    }

    // sort string by freq of chars - better (bucket sort approach)
    public static String sortStringBetter(String str) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : str.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        // bucket: freq -> chars
        Map<Integer, List<Character>> buckets = new HashMap<>();
        for (var e : count.entrySet()) {
            buckets.computeIfAbsent(e.getValue(), k -> new ArrayList<>()).add(e.getKey());
        }

        StringBuilder res = new StringBuilder();
        for (int i = str.length(); i > 0; i--) {
            if (buckets.containsKey(i)) {
                for (char c : buckets.get(i)) {
                    if (c != ' ') {
                        res.append(String.valueOf(c).repeat(i));
                    }
                }
            }
        }
        return res.toString();
    }

    // maximum nesting depth using stack
    public static int maxDepthStack(String str) {
        Deque<Character> stack = new ArrayDeque<>();
        int maxDepth = 0;
        for (char c : str.toCharArray()) {
            if (c == '(') {
                stack.push(c);
                maxDepth = Math.max(maxDepth, stack.size());
            } else if (c == ')' && !stack.isEmpty()) {
                stack.pop();
            }
        }
        return maxDepth;
    }

    // maximum nesting depth without stack
    public static int maxDepthWithoutStack(String str) {
        int depth = 0, maxDepth = 0;
        for (char c : str.toCharArray()) {
            if (c == '(') {
                depth++;
                maxDepth = Math.max(maxDepth, depth);
            } else if (c == ')') {
                depth--;
            }
        }
        return maxDepth;
    }

    // roman to integer conversion - optimal
    public static int romanToIntConv(String roman) {
        Map<Character, Integer> value = Map.of(
                'I', 1, 'V', 5, 'X', 10, 'L', 50,
                'C', 100, 'D', 500, 'M', 1000
        );
        int integer = 0, n = roman.length();
        for (int i = 0; i < n; i++) {
            if (i < n - 1 && value.get(roman.charAt(i)) < value.get(roman.charAt(i + 1))) {
                integer -= value.get(roman.charAt(i));
            } else {
                integer += value.get(roman.charAt(i));
            }
        }
        return integer;
    }

    // atoi implementation
    public static int atoi(String str) {
        str = str.stripLeading();
        if (str.isEmpty()) return 0;

        int sign = 1, i = 0;
        if (str.charAt(0) == '-') {
            sign = -1;
            i++;
        } else if (str.charAt(0) == '+') {
            i++;
        }

        long num = 0; // use long to detect overflow
        while (i < str.length() && Character.isDigit(str.charAt(i))) {
            num = num * 10 + (str.charAt(i) - '0');
            i++;
            if (num > Integer.MAX_VALUE) break;
        }

        num *= sign;
        if (num < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        if (num > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        return (int) num;
    }

    // count substrings -- brute
    public static int cntSubstrings(String str) {
        int n = str.length(), cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 2; j < n; j++) {
                String sub = str.substring(i, j + 1);
                if (sub.contains("a") && sub.contains("b") && sub.contains("c")) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    // count substrings -- optimal 1
    public static int cntSubstrOptimal(String str) {
        int n = str.length();
        Map<Character, Integer> count = new HashMap<>();
        count.put('a', 0);
        count.put('b', 0);
        count.put('c', 0);

        int ans = 0, left = 0;
        for (int right = 0; right < n; right++) {
            count.put(str.charAt(right), count.get(str.charAt(right)) + 1);
            while (count.get('a') > 0 && count.get('b') > 0 && count.get('c') > 0) {
                ans += (n - right);
                count.put(str.charAt(left), count.get(str.charAt(left)) - 1);
                left++;
            }
        }
        return ans;
    }

    // count substrings -- optimal 2
    public static int cntSubstringsOptimal(String str) {
        int n = str.length();
        int[] lastSeen = {-1, -1, -1};
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            lastSeen[str.charAt(i) - 'a'] = i;
            if (lastSeen[0] != -1 && lastSeen[1] != -1 && lastSeen[2] != -1) {
                cnt += 1 + Math.min(lastSeen[0], Math.min(lastSeen[1], lastSeen[2]));
            }
        }
        return cnt;
    }

    // longest palindromic substring -- brute
    public static String longPalindromicSubstrBrute(String str) {
        int n = str.length(), maxLength = 0;
        String best = "";
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String sub = str.substring(i, j + 1);
                if (new StringBuilder(sub).reverse().toString().equals(sub)) {
                    if (sub.length() > maxLength) {
                        maxLength = sub.length();
                        best = sub;
                    }
                }
            }
        }
        return best;
    }

    // longest palindromic substring -- optimal (expand around center)
    public static String longestPalindromicOptimal(String str) {
        int n = str.length(), resLen = 0;
        String res = "";
        for (int i = 0; i < n; i++) {
            // odd length
            int l = i, r = i;
            while (l >= 0 && r < n && str.charAt(l) == str.charAt(r)) {
                if ((r - l + 1) > resLen) {
                    res = str.substring(l, r + 1);
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
            // even length
            l = i;
            r = i + 1;
            while (l >= 0 && r < n && str.charAt(l) == str.charAt(r)) {
                if ((r - l + 1) > resLen) {
                    res = str.substring(l, r + 1);
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
        }
        return res;
    }

    // sum of beauty of all substrings -- brute
    public static int sumBeautyBrute(String str) {
        int n = str.length(), sumVal = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                Map<Character, Integer> freq = new HashMap<>();
                for (int k = i; k <= j; k++) {
                    freq.put(str.charAt(k), freq.getOrDefault(str.charAt(k), 0) + 1);
                }
                int minFreq = Integer.MAX_VALUE, maxFreq = Integer.MIN_VALUE;
                for (int val : freq.values()) {
                    minFreq = Math.min(minFreq, val);
                    maxFreq = Math.max(maxFreq, val);
                }
                if (maxFreq - minFreq != 0) {
                    sumVal += (maxFreq - minFreq);
                }
            }
        }
        return sumVal;
    }

    public static void main(String[] args) {
       String str="abacccccabc";
       System.out.println(sumBeautyBrute(str));
    }
}
