import java.util.*;

public class performXOROnTwoBinaryStrings {
    public static void main(String[] args) throws Exception {
        //I M16 - Exclusive Or

        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        
        String res = "";
        int minLen = Math.min(s1.length(), s2.length());

        String excessZeros = "";
        for (int i = 0; i < Math.abs(s1.length() - s2.length()); i++) {
            excessZeros += "0";
        }
        if(s1.length() > s2.length()) {
            s2 = excessZeros + s2;
        } else {
            s1 = excessZeros + s1;
        }

        minLen = Math.min(s1.length(), s2.length());
        for(int i = minLen-1; i >= 0; i--){
            if(s1.charAt(i) != s2.charAt(i)){
                res = "1" + res;
            }
            else{
                res = "0" + res;
            }
        }
        System.out.println(res);
        sc.close();
    }
}