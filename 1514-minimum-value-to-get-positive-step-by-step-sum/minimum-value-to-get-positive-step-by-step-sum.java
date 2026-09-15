class Solution {
    public int minStartValue(int[] nums) {

        int[] prefix_sum = new int[nums.length];
        prefix_sum[0] = nums[0];

        int ans = nums[0];

        for (int i = 1; i < nums.length; i++) {
            prefix_sum[i] = prefix_sum[i - 1] + nums[i];
            ans = Math.min(ans, prefix_sum[i]);
        }

        if (ans < 0)
            return Math.abs(ans) + 1;

        return 1;
    }
}