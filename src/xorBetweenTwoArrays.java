class TrieNode {
    TrieNode[] child;
    boolean isEnd;

    TrieNode() {
        child = new TrieNode[2];
        child[0] = null;
        child[1] = null;
        isEnd = false;
    }
}

public class Solution {
    public int solve(int[] A, int[] B) {
        TrieNode root = new TrieNode();
        int res = 0;

        for (int x : A)
            insert(root, x);

        for (int x : B)
            res = Math.max(res, search(root, x));

        return res;
    }

    public void insert(TrieNode root, int num) {
        TrieNode curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = ((num >> i) & 1);
            if (curr.child[bit] == null)
                curr.child[bit] = new TrieNode();
            curr = curr.child[bit];
        }
    }

    public int search(TrieNode root, int num) {
        TrieNode curr = root;
        int res = 0;
        for (int i = 31; i >= 0; i--) {
            int x = num;
            int bit = ((x >> i) & 1);
            if (curr.child[1 - bit] != null) {
                res += (1 << i);
                curr = curr.child[1 - bit];
            } else {
                curr = curr.child[bit];
            }
        }
        return res;
    }
}
