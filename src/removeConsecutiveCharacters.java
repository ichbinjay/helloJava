public class Solution {
    public String solve(String A, int B) {
        StringBuilder sb = new StringBuilder();
        int i = 0, n = A.length();
        while (i < n) {
            int j = i + 1;
            while (j < n && A.charAt(j) == A.charAt(i)) {
                j++;
            }
            if (j - i == B) {
                i = j;
            } else {
                sb.append(A.charAt(i));
                i++;
            }
        }
        return sb.toString();
    }
}
