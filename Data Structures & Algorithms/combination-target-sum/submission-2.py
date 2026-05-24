class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(start,path):
            # print(nums[start],path)
            if sum(path) == target:
                ans.append(path[:])
            if not path or sum(path) < target:
                for nxt in range(start, len(nums)):
                    path.append(nums[nxt])
                    dfs(nxt,path)
                    path.pop()      
            return
        ans = []
        dfs(0,[])

        return ans