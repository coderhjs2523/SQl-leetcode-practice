class Solution {
    public int numberOfSubarrays(int[] nums, int k) {

        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 0) {
                nums[i] = 0;
            } else {
                nums[i] = 1;
            }
        }

        int ans = 0;
        int prefix = 0;
        for (int i = 0; i < n; i++) {
            prefix += nums[i];
            int find = prefix - k;

            if (map.containsKey(find)) {
                ans += map.get(find);
            }

            if (map.containsKey(prefix)) {
                map.put(prefix, map.get(prefix) + 1);
            } else {
                map.put(prefix, 1);
            }
        }
        return ans;
    }
}