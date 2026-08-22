class Solution {
    public boolean checkIfPangram(String sentence) {

        HashSet<Character> set = new HashSet<>();

        for(int i=0; i<sentence.length(); i++)
            set.add(sentence.charAt(i));

        if( set.size() == 26)
            return true;
        return false;

        // char[] freq = new char[26];
        // for (int i = 0; i < sentence.length(); i++) {
        //     char ch = sentence.charAt(i);
        //     freq[ch - 'a']++;
        // }
        // for (int i = 0; i < 26; i++) {
        //     if (freq[i] == 0)
        //         return false;
        // }
        // return true;
    }
}