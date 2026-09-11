class Solution {
    public int minStartValue(int[] nums) {

        int startValue = 0;
        int ans = 1;

        for (int ele : nums) {
            startValue += ele;

            if (startValue < 1) {
                ans = Math.max(ans, 1 - startValue);
            }
        }

        return ans;
    }
}