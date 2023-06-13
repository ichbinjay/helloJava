import java.util.Stack;

class Solution {
    class Tuple{
        private int ind;
        private int h;
        Tuple(int ind ,int h){
            this.ind = ind;
            this.h = h;
        }

        public int getInd() {
            return ind;
        }

        public int getH() {
            return h;
        }

    }
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<Tuple> stack = new Stack<>();
        stack.push(new Tuple(0, heights[0]));
        for(int i=1; i < heights.length; i++){
            int start = i;
            while (!stack.isEmpty() && stack.peek().getH() > heights[i]){
                Tuple x = stack.pop();
                int h = x.getH();
                int ind = x.getInd();
                maxArea = Integer.max(maxArea, (i-ind)*h);
                start = ind;
            }
            stack.push(new Tuple(start, heights[i]));
        }
        for (Tuple x : stack) {
            int h = x.getH();
            int ind = x.getInd();
            maxArea = Integer.max(maxArea, (heights.length - ind) * h);
        }
        return maxArea;
    }
}