import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class EncodeAndDecodeStrings {
    public static String encode(String[] strs){
        StringBuilder res = new StringBuilder();
        for(String str : strs){
            res.append(str.length()).append("#").append(str);
        }
        return res.toString();
    }

    public static String[] decode(String str){
        List<String> res = new ArrayList<>();
        int i = 0;
        while(i < str.length()){
            int j = str.indexOf('#', i);
            int len = Integer.parseInt(str.substring(i, j));
            res.add(str.substring(j+1, j+1+len));
            i = j+1+len;
        }
        return res.toArray(new String[0]);
    }
}


class Main{
    public static void main(String[] args) {
        System.out.println(Arrays.toString(EncodeAndDecodeStrings.decode(EncodeAndDecodeStrings.encode(new String[]{"Hello", "World"}))));
    }
}