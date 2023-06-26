class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public int atoi(final String str) {
        int sign = 1, base = 0, i = 0;
        while (i < str.length() && str.charAt(i) == ' ') {
            i++;
        }
        if (i < str.length() && (str.charAt(i) == '-' || str.charAt(i) == '+')) {
            sign = (str.charAt(i++) == '-') ? -1 : 1;
        }
        while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            if (base > Integer.MAX_VALUE / 10 || (base == Integer.MAX_VALUE / 10 && str.charAt(i) - '0' > 7)) {
                if (sign == 1) return Integer.MAX_VALUE;
                else return Integer.MIN_VALUE;
            }
            base = 10 * base + (str.charAt(i++) - '0');
        }
        
        return base * sign;
    }
}


// my approach
//  2023-06-26
class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        if(s.length()==0) return 0;

        boolean sign = false;
        if(s.charAt(0)=='-'){
            s = s.substring(1);
            sign = true;
        }
        else if(s.charAt(0)=='+'){
            s = s.substring(1);
        }
        if(s.length()==0){
            return 0;
        }
        
        String res = "";
        int i=0;
        for(;i<s.length();i++){
            if(s.charAt(i)>='0' && s.charAt(i)<='9'){
                res += s.charAt(i);
            }
            else{
                break;
            }
        }
        if(res.length()==0){
            return 0;
        }


        double intres = 0;
        while(i-- > 0){
            intres += (res.charAt(res.length()-i)-'0')*Math.pow(10,i);
        }
        
        if(sign){
            intres = -intres;
        }
        if(intres>Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }
        else if(intres<Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }
        else{
            return (int)intres;
        }
    }
}