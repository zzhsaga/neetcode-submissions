class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0

        while l < r:
            area = min(heights[l],heights[r])*(r-l)
            ans = max(ans,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans


        