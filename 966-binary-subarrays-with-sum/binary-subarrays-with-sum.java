class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0,1);

        int prefix_sum = 0;
        int ans = 0;

        for (int ele : nums) {

            prefix_sum += ele;
            int find = prefix_sum - goal;

            if (map.containsKey(find)) {
                ans += map.get(find);
            }
            
            if (map.containsKey(prefix_sum)) {
                map.put(prefix_sum, map.get(prefix_sum) + 1);
            } else {
                map.put(prefix_sum, 1);
            }
        }

        return ans;
    }
}