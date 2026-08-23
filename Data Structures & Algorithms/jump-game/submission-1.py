class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums
        # i: jump 1 to nums[i]. if nums[i] can be 0
        # right pointer or right boundary

        # j is reachable, then all the pos before j are reachable as well.
        # :j + 1 is reachable means 0:j is reachable

        # for each pos, 
        # 1. try to expand the rb
        # 2. exit if rb <= nums[i]

        if not nums:
            return False

        rb = 0
        n = len(nums)

        for i, num in enumerate(nums):
            rb = max(rb, i + num)
            if rb >= n - 1:
                return True
            elif rb <= i:
                return False       
        return True
