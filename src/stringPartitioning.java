import java.io.*;
import java.util.*;

public class Solution {
       static int ct=0;
    static int ct1=9999999;
   
    
     public static void func(String s,List<String> al,int ind,int k ){
         if(ind==s.length()){
             ct++;
             ct1=Math.min(k,ct1);
             
         }
             
         for(int i=ind;i<s.length();i++)
             if(al.contains(s.substring(ind,i+1)))
                 func(s,al,i+1,k+1);
         }
    
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            ct=0;
            ct1=9999999;
            int n=sc.nextInt();
            String s=sc.next();
            int n1=sc.nextInt();
            List<String> al=new ArrayList<>();
            for(int i=0;i<n1;i++)
                al.add(sc.next());
            
            func(s,al,0,0);
            System.out.println(ct+" "+(ct1-1));            
        }
    }
}
