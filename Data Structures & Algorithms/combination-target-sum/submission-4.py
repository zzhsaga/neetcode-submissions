class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(start,path,total):
            # print(nums[start],path)
            if total== target:
                ans.append(path[:])
            elif total < target:
                for nxt in range(start, len(nums)):
                    path.append(nums[nxt])
                    total += nums[nxt]
                    dfs(nxt,path,total)
                    path.pop()      
                    total -= nums[nxt]
            return
        ans = []
        dfs(0,[],0)

        return ans