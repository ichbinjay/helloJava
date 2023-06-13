class Solution {
    //create constructor
    public Solution() {
        this.stack = new Stack<>();
        this.minStack = new Stack<>();
    }

    public void push(int x) {
    stack.push(x);
    if(minStack.isEmpty())
        minStack.push(x);
    else{
        if(minStack.top()<x)
            minStack.push(minStack.top());
        else 
            minStack.push(x);
    }
}

    public void pop() {
        if(!minStack.isEmpty() && !stack.isEmpty()){
            minStack.pop();
            stack.pop();
        }
    }

    public int top() {
        if(!stack.isEmpty()){
            return stack.top();
        }
        else return -1;
    }

    public int getMin() {
        if(!minStack.isEmpty()){
            return minStack.pop();
        } 
        else return -1;
    }
}
