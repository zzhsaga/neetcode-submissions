class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area = min during(i,j)*(i-j)
        # for each i, the farest j that heights[j] >= height[i] can yeild the largest area

        ans = 0

        for i,h in enumerate(heights):
            if i > 0 and heights[i] < heights[i-1]:
                continue
            mini = h
            for j in range(i, len(heights)):
                if heights[j] <= mini:
                    mini = heights[j]
                area = mini*(j-i+1)
                ans = max(ans,area)
        
        return ans
