class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int ele : nums){
            if(map.containsKey(ele)){
                int freq = map.get(ele);
                map.put(ele, freq+1);
            }
            else{
                map.put(ele, 1);
            }
        }

        int sum = 0;

        for(int key : map.keySet()){
            if(map.get(key) == 1){
                sum += key;
            }
        }
        return sum;  
    }
}