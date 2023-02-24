import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            long n = sc.nextInt();
            long count = 0;
            for(long i = 5; n/i >= 1; i *= 5){
                count += n/i;
            }
            System.out.println(count);
        }
    }
}