class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # we can turn this problem into put how many comman between the string
        # minimum 1 comma, maximum len(s) - 2 commas
        # the problem is hard if we think about how to find palindrome since palindrome has substring as palindrome, and it related to if we choose the substring of a palindrome, what's the rest part...
        # so we probably should think another way around...
        # we can scan from left to right, simplfied the problem into
        # 1. if I put the comma in this position, is it valid left side?
        # since we didnt scan the right side of this comma yet so we wont know 
        # if the current comma is valid, then we check if the whole right side is a palindrome or we put another comma in the right side to make the substring between comma and the next comma is palindome

        def check(substring):
            # first we have a simplfied version
            return substring == substring[::-1]
        
        def dfs(index,curr,path):
            # print(index,curr,path)
            if check(curr):
                if index >= l:
                    ans.append(path[:])
                else:
                    curr = []
            else:
                return
            for nxt in range(index, l):
                curr.append(s[nxt])
                path.append("".join(curr))
                dfs(nxt + 1,curr,path)
                path.pop()

        l = len(s)
        ans = []
        dfs(0,[],[])
        return ans