class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        nums.sort()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                k = len(nums) - 1
                while k > j:
                    summi = nums[i] + nums[j] + nums[k]
                    if summi == 0:

                        seri = str(nums[i])+str(nums[j])+str(nums[k])
                        if seri not in visited:
                            ans.append([nums[i],nums[j],nums[k]])
                            visited.add(seri)
                        break
                    if summi < 0:
                        break
                    k -= 1
        
        return ans