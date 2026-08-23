class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxlength = 0;
        int j = 0;

        for(int i=0; i<s.length(); i++){
            if(set.contains(s.charAt(i))){
                maxlength = Math.max(maxlength, i-j);
                while(s.charAt(j) != s.charAt(i)){
                    set.remove(s.charAt(j));
                    j++;
                }
                j++;
                set.add(s.charAt(i));
            }
            set.add(s.charAt(i));
        }
        maxlength = Math.max(maxlength, s.length()-j);
        return maxlength;
    }
}