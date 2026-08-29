class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> ans = new ArrayList<>();

        for (int ele : nums) {
            if (map.containsKey(ele)) {
                int freq = map.get(ele);
                map.put(ele, freq+1);
            } else {
                map.put(ele, 1);
            }
        }

        for (int ele : map.keySet()) {
            if (map.get(ele) > (nums.length / 3)) {
                ans.add(ele);
            }
        }
        return ans;
    }
}