import java.io.*;
import java.util.*;

public class Solution {
    public static char function(String s) {
        int[] arr = new int[26];
        for(char ch: s.toCharArray()){
            if(arr[ch-'a']>0) return ch;
            else arr[ch-'a']+=1;
        }
        return '.';
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            String s = sc.next();
            System.out.println(function(s));
        }
    }
}
