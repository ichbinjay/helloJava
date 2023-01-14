class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String res = s.replaceAll("[^a-zA-Z0-9]", "");
        String rev = new StringBuilder(res).reverse().toString();
        return res.equals(rev);
    }
}