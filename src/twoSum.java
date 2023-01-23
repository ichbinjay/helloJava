import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            //if(difference<0) difference = nums[i];

            if(hm.containsKey(difference)){
                return new int[]{i, hm.get(difference)};
            }
            else {
                hm.put(nums[i], i);
            }
        }
        System.out.println(hm);
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.twoSum(new int[]{2, 7, 11, 5}, 9)));
    }
}