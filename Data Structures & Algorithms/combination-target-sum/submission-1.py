class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(curr,path):
            # print(nums[curr],path)
            path.append(nums[curr])
            if sum(path) == target:
                ans.append(path[:])
            elif sum(path) < target:
                for nxt in range(curr, len(nums)):
                    dfs(nxt,path)
            path.pop()
            return
        ans = []
        for i in range(len(nums)):
            dfs(i,[])

        return ans