import java.util.ArrayList;
import java.util.List;

class Solution {
    ArrayList<String> stack = new ArrayList<>();
    List<String> res = new ArrayList<>();
    int n;
    public List<String> generateParenthesis(int n) {
        this.n = n;
        int open = 0, closed = 0;
        backtrack(open, closed);
        return this.res;
    }

    public void backtrack(int open, int closed){
        if(open==n&&closed==n) {
            StringBuilder temp = new StringBuilder();
            for (String e : stack) {
                temp.append(e);
            }
            res.add(temp.toString());
            return;
        }

        if(open<n){
            stack.add("(");
            backtrack(open+1, closed);
            stack.remove(stack.size()-1);
        }
        if(closed<open){
            stack.add(")");
            backtrack(open, closed+1);
            stack.remove(stack.size()-1);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.generateParenthesis(3));
    }
}

