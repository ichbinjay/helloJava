import java.util.*;
class queue
{
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        int testCases = sc.nextInt();
        for(int i=0;i<testCases;i++)
        {
            int type = sc.nextInt();
            if(type==1)
            {
                int val = sc.nextInt();
                q.add(val);
            }
            else if(type==2)
            {
                q.remove();
            }
            else
            {
                System.out.println(q.peek());
            }
        }
        sc.close();
    }
}