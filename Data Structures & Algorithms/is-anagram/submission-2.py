class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = {}

        for char in s:
            if char in memo:
                memo[char] += 1
            else:
                memo[char] = 1

        for char in t:
            if char not in memo:
                return False
            else:
                memo[char] -= 1
        
        for key in memo:
            if memo[key] != 0:
                return False

        return True