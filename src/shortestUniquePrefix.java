class TrieNode{
    TrieNode[] children;
    int freq;
    TrieNode(){
        children = new TrieNode[26];
        freq = 0;
    }

    public void insert(String s){
        TrieNode curr = this;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(curr.children[c - 'a'] == null){
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
            curr.freq++;
        }
    }
}

public class Solution {
    public String[] prefix(String[] a) {
        TrieNode root = new TrieNode();
        for(String s : a){
            root.insert(s);
        }
        String[] res = new String[a.length];
        for(int i = 0; i < a.length; i++){
            TrieNode curr = root;
            String s = a[i];
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < s.length(); j++){
                char c = s.charAt(j);
                sb.append(c);
                curr = curr.children[c - 'a'];
                if(curr.freq == 1){
                    break;
                }
            }
            res[i] = sb.toString();
        }
    return res;
    }
}
