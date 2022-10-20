import java.util.Scanner;

public class timely {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while(n-- > 0){
            if(sc.nextInt() > 30) System.out.println("YES");
            else System.out.println("NO");
        }
        sc.close();
    }
}