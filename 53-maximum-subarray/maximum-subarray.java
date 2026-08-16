class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length, currSum = 0, MaxSum = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            currSum += nums[i];
            MaxSum = Math.max(MaxSum, currSum);
            if (currSum < 0)
                currSum = 0;
        }
        return MaxSum;
    }
}