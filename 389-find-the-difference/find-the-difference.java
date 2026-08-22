class Solution {
    public char findTheDifference(String s, String t) {
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (map1.containsKey(ch)) {
                int freq = map1.get(ch);
                map1.put(ch, freq + 1);
            } else {
                map1.put(ch, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            char ch = t.charAt(i);
            if (map2.containsKey(ch)) {
                int freq = map2.get(ch);
                map2.put(ch, freq + 1);
            } else {
                map2.put(ch, 1);
            }
        }

        for (char key : map2.keySet()) {
            if (!map1.containsKey(key))
                return key;
            if(map1.get(key) != map2.get(key))
                return key;
        }
        return 'a';
    }
}