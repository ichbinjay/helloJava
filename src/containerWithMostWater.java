class Solution {
    public int minNum(int a, int b){
        return a < b ? a : b;
    }
    public int maxArea(int[] height) {
        int l =0, r = height.length-1;
        int max = 0;
        while(l<r){
            int area = 0;
            if(height[l] < height[r]){
                area = height[l] * (r-l);
            }else{
                area = height[r] * (r-l);
            }
            if(area > max){
                max = area;
            }
            if(height[l] < height[r]){
                l++;
            }else{
                r--;
            }
        }
        return max;
    }
}