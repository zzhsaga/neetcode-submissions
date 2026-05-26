class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # it's permutation + dedup
        # for this dedup, one unclear part is if different permuitation subset consider as dup or not
        # from the example, I think the anwser is differnent permutation consider as dup
        # since given 121, but the anwser doesnt have permutation of 1,2,1
        # my thought is we first use a general permutation/back tracking patten, then introduce dedup logic
        # the tricky part is if path in ans cant identify permutations, 
        # so one straight  forward apparoach is sorting nums, than nums became monotonic
        def dfs(curr,path):
            if path not in ans:
                ans.append(path.copy())
            for nxt in range(curr+1,len(nums)):
                path.append(nums[nxt])
                dfs(nxt,path)
                path.pop()
        nums.sort()
        ans = []
        dfs(-1,[])

        return ans


