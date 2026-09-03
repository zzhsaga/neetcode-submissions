class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        memo = {}
        for i in range(len(s)):
            if s[i] in memo:
                memo[s[i]] = i
            else:
                memo[s[i]] = i
        start  = -1
        end = -1

        for i in range(len(s)):
            end = max(end,memo[s[i]])
            if i == end:
                ans.append(end - start)
                start = end
                end = -1
            

        return ans


