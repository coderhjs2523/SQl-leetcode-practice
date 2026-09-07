class Solution {

    public int[] swap(int [] nums, int start, int end){
        while(start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
        return nums;
    }

    public void nextPermutation(int[] nums) {
        
        int n = nums.length-1;
        int pivot = -1;
        int index = -1;

        for(int i = n; i>0; i--){
            if(nums[i] > nums[i-1]){
                pivot = nums[i-1];
                index = i-1;
                break;
            }
        }

        if(pivot == -1){
            swap(nums,0,n);
            return;
        }

        for(int i=n; i>0 ; i--){
            if(nums[i] > pivot){
                int temp = nums[i];
                nums[i] = nums[index];
                nums[index] = temp;
                break;
            }
        }

        swap(nums,index+1,n);
    }
}