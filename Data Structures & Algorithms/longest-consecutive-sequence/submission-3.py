class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        memo = set(nums)
        ans = 1
        
        visited = set()

        for num in memo:
            if num in visited:
                continue
            count = 1
            left = num
            while left - 1 in memo:
                visited.add(left-1)
                left -= 1
                count += 1
            right = num
            while right + 1 in memo:
                visited.add(right+1)
                right += 1
                count += 1
            ans = max(ans, count)

        
        return ans
        