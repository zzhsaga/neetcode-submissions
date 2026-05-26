class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # it's permutation + dedup
        # for this dedup, one unclear part is if different permuitation subset consider as dup or not
        # from the example, I think the anwser is differnent permutation consider as dup
        # since given 121, but the anwser doesnt have permutation of 1,2,1
        # my thought is we first use a general permutation/back tracking patten, then introduce dedup logic
        # the tricky part is if path in ans cant identify permutations, 
        # so one straight  forward apparoach is sorting nums, than nums became monotonic
        # the performance effect of sorting is okay, since it is logn, the main recursion at least in a n^2 level
        # one easy optimization is if in one loop, nxt is same as nxt + 1, in the next turn, they are the same, but if we have something like 1111111, even next turn is the same, the turn next of next turn might be different
        # oh, I see, only the first one need to be consider sincethe first one would finally cause the longest 111... subset and it will cover all shorter once
        # then we might be able to futher optimize, since nums now is mono, we skip during the nxt loop if dup found, it can probably infer that we would never might a dup so if path in ans might not be needed at all
        def dfs(curr,path):
            ans.append(path.copy())
            for nxt in range(curr+1,len(nums)):
                if nxt > curr+1 and nums[nxt] == nums[nxt - 1]:
                    continue
                path.append(nums[nxt])
                dfs(nxt,path)
                path.pop()
        nums.sort()
        ans = []
        dfs(-1,[])

        return ans




