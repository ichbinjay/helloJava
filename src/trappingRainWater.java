class Solution {
    public int trap(int[] arr) {
        int l=0, r=arr.length-1, maxL=arr[l], maxR=arr[r], water=0;
        while( l < r ){
            if( maxL < maxR ){
                l+=1;
                if( arr[l] > maxL ){
                    maxL = arr[l];
                } 
                if(maxL-arr[l] > 0){
                    water += maxL - arr[l];
                }
            }
            else {
                if(arr[r] > maxR){
                    maxR = arr[r];
                }
                if(maxR-arr[r] > 0){
                    water += maxR - arr[r];
                }
            }
        }
        return water;
    }
}