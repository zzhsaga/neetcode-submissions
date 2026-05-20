class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
        # count_S = {}
        # count_T = {}

        # for i in range(len(s)):
        #     if s[i] not in count_S:
        #         count_S[s[i]] = 0
        #     if t[i] not in count_T:
        #         count_T[t[i]] = 0
            
        #     count_S[s[i]] += 1
        #     count_T[t[i]] += 1
        
        # return count_S == count_T