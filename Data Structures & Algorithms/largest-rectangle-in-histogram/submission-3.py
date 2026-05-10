class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area = min during(i,j)*(i-j)
        # for each i, the farest j that heights[j] >= height[i] can yeild the largest area
        n = len(heights)
        ans = 0
        left_most = [-1]*n
        right_most = [n]*n

        stack = []
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            if stack:
                left_most[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)
        print(left_most)
        print(right_most)

        for i in range(n):
            area = heights[i]*(right_most[i] - left_most[i] - 1)
            ans = max(ans, area)
        
        return ans
