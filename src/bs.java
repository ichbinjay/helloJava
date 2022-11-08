import java.util.Scanner;

class bs {
    public static void main(String[] args) {
        /*
         * You are given two arrays of integers a and b. For each element of the second array bj you should find the number of elements in array a that are less than or equal to the value bj.
         * 
         */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] a = new int[n];
        int[] b = new int[m];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }

        for (int i = 0; i < m; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (a[j] <= b[i]) {
                    count++;
                }
            }
            System.out.print(count + " ");
        }
    }
}
