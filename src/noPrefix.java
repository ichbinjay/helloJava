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

    public boolean insert(String s){
        TrieNode curr = this;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(curr.children[c - 'a'] == null){
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
            curr.freq++;
            if(curr.freq > 1){
                return false;
            }
        }
        return true;
    }
}

class Result {

    /*
     * Complete the 'noPrefix' function below.
     *
     * The function accepts STRING_ARRAY words as parameter.
     */

    public static void noPrefix(List<String> words) {
    // Write your code here
    TrieNode root = new TrieNode();
    for(String word : words){
        boolean res = root.insert(root, word);
        if(!res){
            System.out.println("BAD SET");
            System.out.println(word);
            return;
        }
    }
    System.out.println("GOOD SET");
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> words = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        Result.noPrefix(words);

        bufferedReader.close();
    }
}
