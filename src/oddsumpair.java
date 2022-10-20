import java.util.Scanner;

public class oddsumpair {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while(n-- > 0){
            int a = sc.nextInt();int b = sc.nextInt();int c = sc.nextInt();
            if( a+b%2==1 || b+c % 2==1 || c+b%2==1 ) System.out.println("YES");
            else System.out.println("NO");
        }
        sc.close();
    }
}