class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isvalid(char):
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9':
                return True
            else:
                return False
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not isvalid(s[l]):
                l += 1
                continue
            if not isvalid(s[r]):
                r -= 1
                continue
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        