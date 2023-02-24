class Solution {
    public boolean isPalindrome(int x) {
        int res = 0;
        int temp = x;
        while(x != 0){
            int rem = x % 10;
            x /= 10;
            if(res > Integer.MAX_VALUE/10 || (res == Integer.MAX_VALUE/10 && rem > 7)) return false;
            if(res < Integer.MIN_VALUE/10 || (res == Integer.MIN_VALUE/10 && rem < -8)) return false;
            res = res * 10 + rem;
        }
        return res == temp;
    }
}