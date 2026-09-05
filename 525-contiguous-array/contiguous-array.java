class Solution {
    public int findMaxLength(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        map.put(0, -1); 

        int current_sum = 0;
        int maxlength = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] == 0)current_sum += -1;
            else current_sum += 1;

            if(map.containsKey(current_sum))
                maxlength = Math.max(maxlength, i-map.get(current_sum));
            else map.put(current_sum,i);
        }
        return maxlength;
    }
}