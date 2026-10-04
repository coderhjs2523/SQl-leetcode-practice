class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):

        freq = [0] * 101
        ans = []
        l = 0

        for r in range(len(nums)):
            freq[nums[r] + 50] += 1

            if (r-l+1) == k:
                count = 0

                for i in range(50):
                    count += freq[i]

                    if count >= x:
                        value = i - 50
                        ans.append(value)
                        break
                else:
                    ans.append(0)
                
                freq[nums[l] + 50] -= 1
                l += 1

        return ans
                    



# class Solution(object):
#     def getSubarrayBeauty(self, nums, k, x):

#         ans = []
#         l = 0

#         for r in range(len(nums)):

#             if r - l + 1 == k:

#                 temp = nums[l:r+1]
#                 temp.sort()

#                 value = temp[x - 1]

#                 if value < 0:
#                     ans.append(value)
#                 else:
#                     ans.append(0)

#                 l += 1

#         return ans