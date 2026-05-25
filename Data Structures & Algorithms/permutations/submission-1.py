class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            # print(path)
            if not rest:
                ans.append(path[:])
            for num in nums:
                if num not in rest:
                    continue
                path.append(num)
                rest.remove(num)
                dfs(path)
                path.pop()
                rest.add(num)
        
        ans = []
        rest = set(nums)
        l = len(nums)
        dfs([])
        return ans