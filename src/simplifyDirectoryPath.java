import java.util.Stack;

public class Solution{
    public String simplifyPath(String A) {
        Stack<String> stack = new Stack<>();
        String[] arr = A.split("/");
        for(String s: arr){
            if(s.equals("..")){
                if(!stack.isEmpty()) stack.pop();
            }
            else if(s.equals(".") || s.equals("")) continue;
            else stack.push(s);
        }
        return "/"+String.join("/", stack);
    }
}