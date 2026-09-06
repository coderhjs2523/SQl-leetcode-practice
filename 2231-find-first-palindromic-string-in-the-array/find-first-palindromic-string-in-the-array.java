class Solution {
    public String firstPalindrome(String[] words) {

        for (String ele : words) {
            int start = 0;
            int end = ele.length() - 1;
            boolean flag = true;

            while (start < end) {
                if (ele.charAt(start) != ele.charAt(end)) {
                    flag = false;
                    break;
                }
                start++;
                end--;
            }

            if (flag)
                return ele;
        }
        return "";
    }
}