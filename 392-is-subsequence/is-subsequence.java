class Solution {
    public boolean isSubsequence(String s, String t) {

        int p1 = 0, p2 = 0;
        int count = s.length();
        
        while (p1 < s.length() && p2< t.length()) {
            if (s.charAt(p1) == t.charAt(p2)){
                count--;
                p1++;
            }
            p2++;
        }
        return count == 0;
    }
}