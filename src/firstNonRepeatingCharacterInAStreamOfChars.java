import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public String solve(String s) {
        StringBuilder res = new StringBuilder();
        int[] count = new int[26];
        Queue<Character> q =  new LinkedList<Character>();
        for(int i=0; i<s.length();i++){
            count[s.charAt(i)-'a'] +=1;
            q.add(s.charAt(i));

            while(!q.isEmpty()){
                if(count[q.peek()-'a'] > 1)
                    q.remove();
                else
                {
                    res.append(q.peek());
                    break;}
            }
            if(q.isEmpty()) res.append("#");
        }
        return res.toString();
    }
}
