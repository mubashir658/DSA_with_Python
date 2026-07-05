# Title: The k-th Lexicographical String of All Happy Strings of Length n
# Submission ID: 1948307247
# Status: Accepted
# Date: March 14, 2026 at 11:57:12 PM GMT+5:30

class Solution {
    int count = 0;
    String result = "";

    public String getHappyString(int n, int k) {
        backtrack(new StringBuilder(), n, k);
        return result;
    }

    private void backtrack(StringBuilder curr, int n, int k) {
        if (curr.length() == n) {
            count++;
            if (count == k) {
                result = curr.toString();
            }
            return;
        }

        for (char ch : new char[]{'a','b','c'}) {
            if (curr.length() > 0 && curr.charAt(curr.length()-1) == ch) {
                continue;
            }

            curr.append(ch);
            backtrack(curr, n, k);
            curr.deleteCharAt(curr.length()-1);

            if (!result.equals("")) return; 
        }
    }
}
