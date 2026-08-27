class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        farthest = [0,0,0]
        n = len(nums)

        for i,num in enumerate(nums):
            curr = i + nums[i]
            if i > farthest[2]:
                farthest[2] = farthest[0]
                farthest[1] += 1
            if curr > farthest[0]:
                farthest[0] = curr
            

        return farthest[1]