class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                int freq = map.get(nums[i]);
                map.put(nums[i], freq+1);
            }
            else{
                map.put(nums[i], 1);
            }
        }

        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                int freq = map.get(nums[i]);
                if(freq>1){
                    int start = i;
                    for(int end = i+1; end<nums.length; end++){
                        if(nums[end]==nums[i]){
                            if(Math.abs(start-end)<=k)return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}