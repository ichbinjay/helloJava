import java.util.Scanner;

class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long t = sc.nextInt();
        while (t-- > 0) {
            long n = sc.nextInt();
            long d = sc.nextInt();
            d = d % n;
            long[] arr = new long[(int) n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            rotate(arr, 0, n-1);
            rotate(arr, 0, d-1);
            rotate(arr, d, n-1);

            for (int i = 0; i < n; i++) {
                System.out.print(arr[i] + " ");
            }
        }
    }

    public static void rotate ( long[] arr, long start, long end){
        long temp;
        while (start < end) {
            temp = arr[(int) start];
            arr[(int) start] = arr[(int) end];
            arr[(int) end] = temp;
            start++;
            end--;
        }
    }
}