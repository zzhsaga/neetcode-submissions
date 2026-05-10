class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        s = s.lower()
        
        l = 0
        r = len(s) - 1

        while l < r:
            if not alphaNum(s[l]):
                l += 1
                continue
            if not alphaNum(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                print(s[l],s[r])
                return False
            l += 1
            r -= 1
        
        return True