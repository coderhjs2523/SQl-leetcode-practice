class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int ans = 0;
        int prefix_sum = 0;
        for (int ele : nums) {
            prefix_sum += ele;
            int find = prefix_sum - k;
            if (map.containsKey(find)) {
                int freq = map.get(find);
                ans += freq;
            }
            if (map.containsKey(prefix_sum)) {
                // If it exists, get the current count and add 1
                map.put(prefix_sum, map.get(prefix_sum) + 1);
            } else {
                // If it's new, start the count at 1
                map.put(prefix_sum, 1);
            }

        }
        return ans;
    }
}