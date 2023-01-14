import java.util.*;

public class infixToPostfix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        itp(s);
        sc.close();
    }

    public static void itp(String s){
        Stack<Character> stack = new Stack<Character>();
        for(char i : s.toCharArray()){
            if(Character.isLetterOrDigit(i)){
                System.out.print(i);
            }else if(i == '('){
                stack.push(i);
            }else if(i == ')'){
                while(!stack.isEmpty() && stack.peek() != '('){
                    System.out.print(stack.pop());
                }
                if(!stack.isEmpty() && stack.peek() != '('){
                    return;
                }else{
                    stack.pop();
                }
            }else{
                while(!stack.isEmpty() && precedence(i) <= precedence(stack.peek())){
                    System.out.print(stack.pop());
                }
                stack.push(i);
            }
        }
        while(!stack.isEmpty()){
            System.out.print(stack.pop());
        }
    }

    public static int precedence(char c){
        switch(c){
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
        }
        return -1;
    }
}
