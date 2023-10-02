class Solution {
    public long findAverage(int i, int j, int[] nums) {
        long sum = 0;
        for(int k = i; k <= j; k++) sum += nums[k];
        return sum / (j - i + 1);
    }

    public int[] getAverages(int[] nums, int k) {
        int len = nums.length;
        int[] averages = new int[len];
        for(int i=0; i < len; i++) {
            if(i-k <0 || i+k >= len) {
                averages[i] = -1;
            } else {
                long res = findAverage(i-k, i+k, nums);
                if(res > Integer.MAX_VALUE) {
                    averages[i] = -1;
                } else {
                    averages[i] = (int) res;
                }
            }
        }
        return averages;
    }
}
