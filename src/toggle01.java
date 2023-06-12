import java.io.*;
import java.util.*;

public class Solution{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            long n = sc.nextLong();
            int q = sc.nextInt();
            TreeSet<Integer> ts = new TreeSet<>();
            for(int i=0;i<1;i++){
                int type = sc.nextInt(), ind = sc.nextInt();
                if(type==1){
if(ts.contains(ind)) ts.remove(ind);
else ts.add(ind);
                }
                else{
                    int floor, ceil;
                    try{
                        floor = ts.floor(ind);
                    }
                    catch(Exception e){
                        floor = Integer.MAX_VALUE;
                    }
                    try{
                        ceil = ts.ceiling(ind);
                    }
                    catch(Exception e){
                        ceil = Integer.MAX_VALUE;
                    }
                    if(ts.isEmpty()) System.out.println(-1);
                    else System.out.println(Math.min(Math.abs(ind-floor), Math.abs(ind-ceil)));
                }
            }
        }
    }
}
