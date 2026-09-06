class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> map = new HashMap<>();
        List<String> ans = new ArrayList<>();

        for (String ch : words) {
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
        }

        for (int i = 0; i < k; i++) {
            int maxfreq = 0;
            String temp = "";
            for (String key : map.keySet()) {
                int currentFreq = map.get(key);
                if (currentFreq > maxfreq) {
                    maxfreq = map.get(key);
                    temp = key;
                }
                else if (currentFreq == maxfreq) {
                    if (temp.isEmpty() || key.compareTo(temp) < 0) {
                        temp = key;
                    }
                }
            }
            ans.add(temp);
            map.remove(temp);
        }
        return ans;
    }
}