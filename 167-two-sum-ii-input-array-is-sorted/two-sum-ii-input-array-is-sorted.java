class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int start = 0;
        int end = n-1;
        int [] ans = new int [2];
        while(start < end){
            if(numbers[start] + numbers[end] == target){
                ans[0] = start + 1;
                ans[1] = end + 1;
                break;
            }
            else if(numbers[start] + numbers[end] > target){
                end = end - 1;
            }
            else{
                start++;
            }
        }
        return ans;
    }
}