 int[] answerQueries(ArrayList<Query> queries, int N){
        TreeSet<Integer> set =   new TreeSet();
        ArrayList<Integer> arr = new ArrayList();
        for(Query q: queries){
            if(q.getType() == 1){
                set.add(q.getIndex());
            }else{
                Integer val = set.ceiling(q.getIndex());
                if(val==null){
                    arr.add(-1);
                }else{
                    arr.add(val);
                }
            }
       }
       int[] result = new int[arr.size()];
       for(int i=0;i<arr.size();i++){
            result[i] = arr.get(i);
        }
        return result;
    }