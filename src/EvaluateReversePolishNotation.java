class Solution {
    public int evalRPN(String[] tokens) {
        int[] stack = new int[tokens.length];
        int top = -1;
        for (String token : tokens) {
            switch (token) {
                case "+" -> {
                    stack[top - 1] += stack[top];
                    top--;
                }
                case "-" -> {
                    stack[top - 1] -= stack[top];
                    top--;
                }
                case "*" -> {
                    stack[top - 1] *= stack[top];
                    top--;
                }
                case "/" -> {
                    stack[top - 1] /= stack[top];
                    top--;
                }
                default -> stack[++top] = Integer.parseInt(token);
            }
        }
        return stack[top];
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] tokens = {"2", "1", "+", "3", "*"};
        System.out.println(solution.evalRPN(tokens));
    }
}
