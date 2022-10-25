import java.util.Scanner;

public class Diffconsec {
    public static boolean vowelcheck(char w, char x) {
        //vowels = {a, e, i, o, u, y}
        if(w == 'a'){
            if(x == 'e' || x == 'i' || x == 'o' || x == 'u' || x == 'y'){
                return true;
            }
        }
        else if(w == 'e'){
            if(x == 'a' || x == 'i' || x == 'o' || x == 'u' || x == 'y'){
                return true;
            }
        }
        else if(w == 'i'){
            if(x == 'a' || x == 'e' || x == 'o' || x == 'u' || x == 'y'){
                return true;
            }
        }
        else if(w == 'o'){
            if(x == 'a' || x == 'e' || x == 'i' || x == 'u' || x == 'y'){
                return true;
            }
        }
        else if(w == 'u'){
            if(x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'y'){
                return true;
            }
        }
        else if(w == 'y'){
            if(x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u'){
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
            String s = sc.next();
            for (int i = 0; i < s.length() - 1; i++) {
                if (s.charAt(i) == s.charAt(i + 1) || vowelcheck(s.charAt((i)), s.charAt(i + 1))) {
                    System.out.println("No");
                    System.exit(0);
                }
            }
            System.out.println("Yes");
        sc.close();
    }
}