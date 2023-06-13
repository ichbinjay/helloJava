class Result {

    /*
     * Complete the 'getMax' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts STRING_ARRAY operations as parameter.
     */

    public static List<Integer> getMax(List<String> operations) {
    // Write your code here
        Stack<Integer> stack = new Stack<Integer>();
        List<Integer> res = new ArrayList<Integer>();
        for(int i=0; i<operations.size(); i++){
        String[] op = operations.get(i).split(" ");
        if(op[0].equals("1")){
            stack.push(Integer.parseInt(op[1]));
        }
        else if(op[0].equals("2")){
            stack.pop();
        }
        else if(op[0].equals("3")){
            int max = stack.peek();
            for(int j=0; j<stack.size(); j++){
                if(stack.get(j) > max){
                    max = stack.get(j);
                }
            }
            res.add(max);
        }
    }
    return res;
    }
}