import java.util.*;

class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int n = sc.nextInt();
            int[][] arr = new int[n][n];
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    arr[i][j] = sc.nextInt();
                }
            }
            for(int k = -n+1; k < n; k++){
                int sum = 0;
                for(int i = 0; i < n; i++){
                    for(int j = 0; j < n; j++){
                        if(i - j == k){
                            sum += arr[i][j];
                        }
                    }
                }
                System.out.print(sum + " ");
            }
            
        System.out.println();
        }
        sc.close();
    }
}