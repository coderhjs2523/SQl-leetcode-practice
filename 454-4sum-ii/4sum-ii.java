class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        HashMap<Integer, Integer> map1 = new HashMap<>();//nums1+nums2
        HashMap<Integer, Integer> map2 = new HashMap<>();//nums3+nums4

        for (int num1 : nums1) {
            for (int num2 : nums2) {
                if (map1.containsKey(num1 + num2)) {
                    int freq = map1.get(num1 + num2);
                    map1.put(num1 + num2, freq + 1);
                } else {
                    map1.put(num1 + num2, 1);
                }
            }
        }

        for (int num3 : nums3) {
            for (int num4 : nums4) {
                if (map2.containsKey(num3 + num4)) {
                    int freq = map2.get(num3 + num4);
                    map2.put(num3 + num4, freq + 1);
                } else {
                    map2.put(num3 + num4, 1);
                }
            }
        }

        int count = 0;
        for (int ele : map1.keySet()) {
            if (map2.containsKey(-ele)) {
                count += map1.get(ele) * map2.get(-ele);
            }
        }
        return count;
    }
}