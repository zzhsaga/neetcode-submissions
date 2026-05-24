class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # for each item, we want to search every candidates that valid
        def dfs(curr, path, total):
            # print(curr,path)
            if total > target:
                return
            if total == target and path not in ans:
                ans.append(path[:])
                return
            for nxt in range(curr + 1,len(candidates)):
                if nxt > curr + 1 and candidates[nxt] == candidates[nxt-1]:
                    continue
                if total +  candidates[nxt]> target:
                    return
                path.append(candidates[nxt])
                total += candidates[nxt]
                dfs(nxt,path,total)
                path.pop()
                total -= candidates[nxt]
        candidates.sort()
        ans = []
        dfs(-1,[], 0)

        return ans
