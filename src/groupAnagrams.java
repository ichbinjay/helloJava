import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<String> sorted_strs = new ArrayList<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            sorted_strs.add(new String(chars));
        }
        Dictionary<String, List<String>> dict = new Hashtable<>();
        for(int i = 0;  i < sorted_strs.size(); i++){
            String sorted_str = sorted_strs.get(i);
            if(dict.get(sorted_str) != null){
                dict.get(sorted_str).add(strs[i]);
            }else{
                List<String> list = new ArrayList<>();
                list.add(strs[i]);
                dict.put(sorted_str, list);
            }
        }
        List<List<String>> result = new ArrayList<>();
        Enumeration<List<String>> values = dict.elements();
        while (values.hasMoreElements()) {
            List<String> value = values.nextElement();
            result.add(value);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(solution.groupAnagrams(strs));
    }
}