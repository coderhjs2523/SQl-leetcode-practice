class Solution {
    public int findMiddleIndex(int[] nums) {

        int n = nums.length;

        if (n == 1)
            return 0;

        int prefix = 0;

        for (int i = 0; i < n; i++)
            prefix += nums[i];

        int left_sum = 0;

        for (int i = 0; i < n; i++) {
            int right_sum = prefix - nums[i] - left_sum;

            if (right_sum == left_sum)
                return i;

            left_sum += nums[i];
        }

        return -1;
    }
}