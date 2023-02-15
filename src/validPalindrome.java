class Solution {
    public boolean isPalindrome(String s) {
        String res = "";
        for(int i = 0; i < s.length(); i++){
            if((s.charAt(i) >= 'a' && s.charAt(i) <= 'z') || (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') || (s.charAt(i) >= '0' && s.charAt(i) <= '9')){
                if(s.charAt(i) >= 'A' && s.charAt(i) <= 'Z'){
                    res += (char)(s.charAt(i) + 32);
                }else{
                    res += s.charAt(i);
                }
            }
        }
        int l = 0, r = res.length()-1;
        while(l<r){
            if(res.charAt(l) != res.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}