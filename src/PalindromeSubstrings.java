class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        for(int i=0; i < s.length(); i++){
            int l = i, r = i;
            while(l > -1 && r < s.length() && s.charAt(l) == s.charAt(r)){
                l--;
                r++;
                count++;
            }

            l = i;
            r = i+1;
            while(l > -1 && r < s.length() && s.charAt(l) == s.charAt(r)){
                l--;
                r++;
                count++;
            }
        }
        return count;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countSubstrings("abc"));
    }
}