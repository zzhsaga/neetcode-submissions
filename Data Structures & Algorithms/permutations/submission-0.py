class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            # print(path)
            if len(path) == l:
                ans.append(path[:])
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                dfs(path)
                path.pop()
        
        ans = []
        l = len(nums)
        dfs([])
        return ans