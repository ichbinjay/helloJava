import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String roman = sc.next();
        int[] nums = new int[roman.length()];
        for(int i=0;i<roman.length();i++){
            switch(roman.charAt(i)){
                case 'I':
                    nums[i] = 1;
                    break;
                case 'V':
                    nums[i] = 5;
                    break;
                case 'X':
                    nums[i] = 10;
                    break;
                case 'L':
                    nums[i] = 50;
                    break;
                case 'C':
                    nums[i] = 100;
                    break;
                case 'D':
                    nums[i] = 500;
                    break;
                case 'M':
                    nums[i] = 1000;
                    break;
            }
        }
        
        int sum = 0;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i] < nums[i+1]){
                sum -= nums[i];
            }
            else{
                sum += nums[i];
            }
        }
        sum += nums[nums.length-1];
        System.out.println(sum);
    }
}