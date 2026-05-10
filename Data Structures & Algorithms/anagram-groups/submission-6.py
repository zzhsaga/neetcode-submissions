class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        memo = {}
        ans = []

        for s in strs:
            sorted_str_list = sorted(s)
            sorted_str = "".join(sorted_str_list)
            if sorted_str in memo:
                index = memo[sorted_str]
                ans[index].append(s)
            else:
                memo[sorted_str] = len(ans)
                ans.append([s])
        return ans
        
        