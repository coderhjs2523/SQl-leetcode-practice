class Solution {
    public String reverseVowels(String s) {
        char[] arr = s.toCharArray();
        String match = "aeiouAEIOU";
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            while (start < end && match.indexOf(arr[start]) == -1)
                start++;
            while (end > start && match.indexOf(arr[end]) == -1)
                end--;

            char temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
        return new String(arr);
    }
}