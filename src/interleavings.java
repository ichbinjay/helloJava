import java.io.*;
import java.util.*;

public class Solution {
    public static void solve(String s1, String s2, int i, int j, String ans){
        
        if(i==0 && j==0){
            //base case
        }
        
        if(i==0 && j!=0){
            //edge case1
        }
        if(i!=0 && j==0){
            //edge case2
        }
        if(s1.charAt(i)<s2.charAt(j)){
            solve(s1, s2, i+1, j, ans+s.charAt(i));
            solve(s1, s2, i, j+1, ans+s.charAt(j));
        }else{
            solve(s1, s2, i, j+1, ans+s.charAt(j));
            solve(s1, s2, i+1, j, ans+s.charAt(i));
        }
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}