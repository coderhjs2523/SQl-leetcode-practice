class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[k];

        for (int ele : nums) {
            if (map.containsKey(ele)) {
                int freq = map.get(ele);
                map.put(ele, freq + 1);
            } else {
                map.put(ele, 1);
            }
        }
        for (int i = 0; i < k; i++) {
            int maxfreq = -1;
            int fill = -1;
            for (int key : map.keySet()) {
                if (map.get(key) >= maxfreq) {
                    maxfreq = map.get(key);
                    fill = key;
                }
            }
            ans[i] = fill;
            map.remove(fill);
        }
        return ans;
    }
}