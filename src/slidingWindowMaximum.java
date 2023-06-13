import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Deque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int l=0, r=0;
        ArrayList<Integer> res = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>();
        while(r<nums.length){
            while(q.isEmpty() && nums[q.getLast()] < nums[r])
                q.pop();
            q.addLeft(r);

            if(l > q.getFirst())
                q.removeFirst();

            if(r+1 >= k){
                res.add(nums[q.getFirst()]);
                l+=1;
            }
            r+=1;
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}