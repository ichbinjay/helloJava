import java.util.*;

public class StarString {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        for(int i = 0; i < s.length()-1; i++){
            if(s.charAt(i)==s.charAt(i+1) || s.charAt(i)=="a" || s.charAt(i)=="e" || s.charAt(i)=="i" || s.charAt(i)=="o" || s.charAt(i)=="u" || s.charAt(i)=="y"){
                System.out.println("NO");
                System.exit(0);
            }
        }

    }
}
