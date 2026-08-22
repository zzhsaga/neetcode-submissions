class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for each pos, what's the largest prefix array
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        prev_sum = 0
        ans = nums[0]

        for i in range(len(nums)):
            prev_sum = max(nums[i], nums[i] + prev_sum)
            ans = max(ans,prev_sum)
        
        return ans