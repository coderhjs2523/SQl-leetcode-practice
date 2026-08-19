class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int window = 0;
        for(int i=0; i<k; i++){
            window += arr[i];
        }

        int count = 0;
        int avg = window/k;

        if(avg >= threshold)count++;

        for(int i=k; i<arr.length; i++){
            window -= arr[i-k];
            window += arr[i];
            if(window/k >= threshold)count++;
        }
        return count;
    }
}