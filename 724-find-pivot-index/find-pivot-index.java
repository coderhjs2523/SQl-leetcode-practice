class Solution {
    public int pivotIndex(int[] nums) {

        int n = nums.length;
        int prefix_sum = 0, leftSum = 0;

        for (int i = 0; i < n; i++)
            prefix_sum += nums[i];
        
        for (int i = 0; i < n; i++) {
            
            int rightSum = prefix_sum - leftSum - nums[i];

            if (leftSum == rightSum)
                return i;

            leftSum += nums[i];
        }
        return -1;
    }
}