import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();
        while(t-- > 0){
            long a = sc.nextLong(), b = sc.nextLong();
            long x, y;
            if(a > b){
                x = a;
            }
            else{
                x = b;
            }

            if(a<b){
                y = a;
            }
            else{
                y = b;
            } 
            
            while(y > 0){
                long temp = y;
                y = x % y;
                x = temp;
            }
            long hcf = x;
            long lcm = (a*b)/hcf;
            System.out.println(lcm + " " + hcf);
        }
    }
}