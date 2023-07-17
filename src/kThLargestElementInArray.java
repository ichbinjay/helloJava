import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for(int i=0;i<nums.length;i++){
            pq.add(nums[i]);
            if(pq.size()>k){
                pq.poll();
            }
        }
        return pq.peek();
    }
}

//poll vs peek vs remove
//poll() - Retrieves and removes the head of this queue, or returns null if this queue is empty.
//peek() - Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.
//remove() - Retrieves and removes the head of this queue. This method differs from poll only in that it throws an exception if this queue is empty.