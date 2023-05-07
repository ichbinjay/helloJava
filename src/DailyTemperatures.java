import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;


class Main {
    int[] dailyTemperatures(int[] temps) {
        int n = temps.length;
        int[] ans = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && temps[i] >= temps[stack.peek()]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? 0 : stack.peek() - i;
            stack.push(i);
        }
        return ans;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};
        System.out.println(Arrays.toString(solution.dailyTemperatures(temps)));
    }
}
