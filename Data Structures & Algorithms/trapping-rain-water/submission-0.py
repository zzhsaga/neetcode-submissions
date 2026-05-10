class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        l_max = [-1]*len(height)
        r_max = [-1]*len(height)

        curr_max = 0
        for i in range(len(height)):
            if height[i] > curr_max:
                curr_max = height[i]
            l_max[i] = curr_max
        curr_max = 0
        for j in range(len(height)-1, -1, -1):
            if height[j] > curr_max:
                curr_max = height[j]
            r_max[j] = curr_max

        
        
        for k in range(len(height)):
            curr = min(l_max[k],r_max[k])
            if curr > height[k]:
                ans += curr - height[k]


        return ans