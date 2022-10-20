import java.util.Scanner;

public class Diffconsec {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while(n-- > 0){
            int length = sc.nextInt();
            String s = sc.next();
            System.out.println(s);
            int similarChars = 0;
            for(int i=0; i<length-1; i++){
                if(s.charAt(i) == s.charAt(i+1)) similarChars++;
            }
            System.out.println(similarChars);
        }
        sc.close();
    }
}