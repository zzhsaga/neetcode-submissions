class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = [0]*26
        
        for char in s:
            memo[ord(char)-ord('a')] += 1
        for char in t:
            memo[ord(char)-ord('a')] -= 1
        for m in memo:
            if m != 0:
                return False
        return True        
