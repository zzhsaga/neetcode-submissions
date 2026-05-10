class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for a in range(len(nums) - 2):
            l = a + 1
            r = len(nums) - 1
            while l < r:
                sumi = nums[l] + nums[r] + nums[a]
                if sumi == 0:
                    curr = [nums[a],nums[l],nums[r]]
                    if curr not in ans:
                        ans.append([nums[a],nums[l],nums[r]])
                    l += 1
                elif sumi < 0:
                    l += 1
                else:
                    r -= 1
        
        return ans