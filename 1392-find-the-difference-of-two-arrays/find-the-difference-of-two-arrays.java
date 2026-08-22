class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();

        for(int ele : nums1)
            set1.add(ele);

        for(int ele : nums2)
            set2.add(ele);
        
        for(int ele : set1){
            if(!set2.contains(ele))
                list1.add(ele);
        }
        ans.add(list1);

        for(int ele : set2){
            if(!set1.contains(ele))
                list2.add(ele);
        }
        ans.add(list2);
        return ans;
    }
}