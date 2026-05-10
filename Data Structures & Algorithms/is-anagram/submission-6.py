class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        origin = ord('a')
        if len(s) != len(t):
            return False
        memo = [0]*26
        for i in range(len(s)):
            memo[ord(s[i]) - origin] += 1
            memo[ord(t[i]) - origin] -= 1
        for m in memo:
            if m != 0:
                return False
        return True