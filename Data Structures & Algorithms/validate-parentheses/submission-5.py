class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for char in s:
            if char in open_close:
                stack.append(char)
            else:
                if not stack or open_close[stack.pop()] != char:
                    return False
        
        return not stack
                               
        