import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        int c1=0,c2=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){c1++;c2++;}
            else if(s.charAt(i)==')'){c1--;c2--;}
            else{c1--;c2++;}
            if(c2<0){System.out.println("false"); return;}
            c1=Math.max(c1,0);
        }
        if(c1==0)System.out.println("true");
        else System.out.println("false");
    }
}
