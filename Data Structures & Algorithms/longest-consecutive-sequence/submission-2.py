class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        curr_len = 1
        ans = 0

        if len(nums) < 2:
            return len(nums)

        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if diff < 2:
                curr_len += diff
                ans = max(ans,curr_len)
                print(curr_len,nums[i])
            else:
                curr_len = 1
        
        return ans
        