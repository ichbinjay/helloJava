class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int windowSize = s1.length();
        for (int i = 0; i < s2.length()-windowSize+1; i++) {
            String[] s1Arr = s1.split("");
            Arays.sort(s1Arr);
            sortedS1 = String.join("", s1Arr);

            String[] s2Arr = s2.substring(i, i+windowSize).split("");
            Arrays.sort(s2Arr);
            sortedS2 = String.join("", s2Arr);

            if (sortedS1.equals(sortedS2)) return true;
        }
    }
}

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int windowSize = s1.length();
        int[] s1Arr = new int[26];
        for(int i=0;i<windowSize;i++){
            s1Arr[s1.charAt(i)-'a']++;
        }

        for(int i=0;i<s2.length()-windowSize+1;i++){
            int[] s2Arr = new int[26];
            for(int j=i;j<i+windowSize;j++){
                s2Arr[s2.charAt(j)-'a']++;
            }
            if(Arrays.equals(s1Arr,s2Arr)) return true;
        }
        return false;
    }
}