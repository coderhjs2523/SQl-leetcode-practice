class Solution {
    public String reverseOnlyLetters(String s) {

        char [] arr = s.toCharArray();
        
        int start = 0;
        int end = s.length()-1;

        while(start<end){
            char ch_start = arr[start];
            if(!Character.isLetter(ch_start)){
                start++;
                continue;
            }

            char ch_end = arr[end];
            if(!Character.isLetter(ch_end)){
                end--;
                continue;
            }

            char temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }

        return new String(arr);
    }
}