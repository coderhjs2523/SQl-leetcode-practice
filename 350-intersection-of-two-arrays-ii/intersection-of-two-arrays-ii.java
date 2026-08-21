class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {

        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> map2 = new HashMap<>();
        ArrayList<Integer> ans = new ArrayList<>();

        for (int ele : nums1){
            if(map1.containsKey(ele)){
                int freq = map1.get(ele);
                map1.put(ele, freq + 1);
            }
            else{
                map1.put(ele, 1);
            }
        }

        for (int ele : nums2){
            if(map2.containsKey(ele)){
                int freq = map2.get(ele);
                map2.put(ele, freq + 1);
            }
            else{
                map2.put(ele, 1);
            }
        }


        for (int key : map1.keySet()){
            if(map2.containsKey(key)){
                int freq1 = map1.get(key);
                int freq2 = map2.get(key);

                int min = Math.min(freq1, freq2);

                for(int i=0; i<min; i++)ans.add(key); 
            }
        }
            
        return ans.stream()
                .mapToInt(Integer::intValue)
                .toArray();

    }
}