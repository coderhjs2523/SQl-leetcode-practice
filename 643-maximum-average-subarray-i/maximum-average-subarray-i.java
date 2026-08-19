class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n= nums.length;
        int window = 0;
        for(int i=0;i<k;i++) window += nums[i];

        int maxsum = window;
        int start = 0;
        for(int i = k; i<n; i++){
            window -= nums[start];
            start++;

            window += nums[i];

            maxsum = Math.max(window, maxsum);
        }
        return (double)maxsum/k;
    }
}