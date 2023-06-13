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

/*
how to solve this problem?
1) create a monotonically increasing stack. which means that the stack will always be in increasing order.
2) if current element is less than stack top, then keep popping the stack until the stack top is less than current element.
3) in this popping part, we will use two vars, height and index. height is the height of that histogram and index is basically the point(probably behind)
from where we include in the map.
4) we are using a start var to keep track of the index from where we are starting to include in the map.
5) last fop loop is to calculate the area os stack elements which survived the popping part.
*/