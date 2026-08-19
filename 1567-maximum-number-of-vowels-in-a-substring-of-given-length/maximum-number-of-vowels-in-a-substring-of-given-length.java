class Solution {
    public int maxVowels(String s, int k) {
        int count = 0;
        int maxcount = 0;
        String vowel = "aeiou";

        for (int i=0;i<k;i++){
            if(vowel.contains(String.valueOf(s.charAt(i)))){
                count++;
                maxcount = Math.max(maxcount, count);
            }
        }

        for(int i = k; i<s.length(); i++){
            if(vowel.contains(String.valueOf(s.charAt(i-k)))){
                count--;
            }
            if(vowel.contains(String.valueOf(s.charAt(i)))){
                count++;
                maxcount = Math.max(maxcount, count);
            }
        }
        return maxcount;
    }
}