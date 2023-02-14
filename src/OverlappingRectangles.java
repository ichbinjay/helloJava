import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int x = 0; x < t; x++) {
            long x1bl = sc.nextInt();
            long y1bl = sc.nextInt();
            long x1tr = sc.nextInt();
            long y1tr = sc.nextInt();
            long x2bl = sc.nextInt();
            long y2bl = sc.nextInt();
            long x2tr = sc.nextInt();
            long y2tr = sc.nextInt();

            long area1 = Math.abs((x1tr - x1bl) * (y1tr - y1bl));

            long area2 = Math.abs((x2tr - x2bl) * (y2tr - y2bl));

            long x3bl = Math.max(x1bl, x2bl);
            long y3bl = Math.max(y1bl, y2bl);
            long x3tr = Math.min(x1tr, x2tr);
            long y3tr = Math.min(y1tr, y2tr);
            long area3 = 0;
            if (x3bl < x3tr && y3bl < y3tr) {
                area3 = (x3tr - x3bl) * (y3tr - y3bl);
            }
            System.out.println(area1 + area2 - area3);
        }
    }
}