class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = [0]*26
        
        for i in range(len(s)):
            memo[ord(s[i])-ord('a')] += 1
            memo[ord(t[i])-ord('a')] -= 1
        for m in memo:
            if m != 0:
                return False
        return True        
