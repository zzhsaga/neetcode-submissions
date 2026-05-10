class Solution:
    def isValid(self, s: str) -> bool:
        memo = {'(': ')', '{': '}', '[' : ']'}

        stack = []

        for c in s:
            if c in memo:
                stack.append(c)
            else:
                if not stack or memo[stack.pop()] != c:
                    return False
        
        return len(stack) == 0