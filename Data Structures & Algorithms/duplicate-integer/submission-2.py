class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        memo = set()

        for num in nums:
            if num in memo:
                ans = True
                break
            else:
                memo.add(num)
        
        return ans
        