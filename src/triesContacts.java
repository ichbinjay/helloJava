import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

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

    public static void main(String[] args) throws IOException {
        TrieNode root = new TrieNode();
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, n).forEach(nItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                String op = firstMultipleInput[0];

                String contact = firstMultipleInput[1];

                if(op.equals("add")){
                    root.insert(contact);
                }else{
                    TrieNode curr = root;
                    for(int i = 0; i < contact.length(); i++){
                        char c = contact.charAt(i);
                        if(curr.children[c - 'a'] == null){
                            System.out.println(0);
                            break;
                        }
                        curr = curr.children[c - 'a'];
                        if(i == contact.length() - 1){
                            System.out.println(curr.freq);
                        }
                    }
                }
                
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}


