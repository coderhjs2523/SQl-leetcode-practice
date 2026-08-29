class Solution {
    public List<String> findRepeatedDnaSequences(String s) {

        HashSet<String> set = new HashSet<>();
        HashSet<String> repeat = new HashSet<>();
        List<String> ans = new ArrayList<>();

        if(s.length()<10){
            return ans;
        }

        String str = s.substring(0, 10);
        set.add(str);

        for (int i = 10; i < s.length(); i++) {
            str += s.charAt(i);
            str = str.substring(1);

            if (set.contains(str))
                repeat.add(str);
            else
                set.add(str);
        }
        ans.addAll(repeat);
        return ans;
    }
}