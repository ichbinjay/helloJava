import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int x = 0; x < t; x++) {
            int n = sc.nextInt();
            int[][] arr = new int[n][n];
            
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            int[][] arr2 = new int[n][n];
            System.out.println("Test Case #" + (x + 1) + ": ");
            for (int i = 0; i < n; i++) {
                for (int j = arr.length-1; j > -1; j--) {
                    arr2[i][arr.length-1-j] = arr[j][i];
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(arr2[i][j] + " ");
                }
                System.out.println();
            }
        }
    }
}