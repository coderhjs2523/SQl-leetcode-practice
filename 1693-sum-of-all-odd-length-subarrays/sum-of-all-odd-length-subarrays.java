class Solution {
    public int sumOddLengthSubarrays(int[] arr) {

        int n = arr.length;

        int[] prefix = new int[n];
        prefix[0] = arr[0];

        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {

            for (int j = i; j < n; j++) {

                int length = j - i + 1;

                if (length % 2 == 1) {

                    if (i == 0)
                        ans += prefix[j];
                    else
                        ans += prefix[j] - prefix[i - 1];
                }
            }
        }

        return ans;
    }
}