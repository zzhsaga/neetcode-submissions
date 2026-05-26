class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # still permutation, but we dont read from a list, the contraints are two
        # we have n ( and )
        # ( number must be >= ) as always
        def dfs(path):
            if len(path) == 2*n:
                ans.append(''.join(path))
            for nxt in ['(',')']:
                if counter[nxt] < n:
                    if nxt == ')' and counter[nxt] >= counter['(']:
                        continue
                    counter[nxt]+=1
                    path.append(nxt)
                    dfs(path)
                    counter[nxt]-=1
                    path.pop()

        counter = {'(':0,')':0}
        ans = []

        dfs([])
        print(ans)

        return ans

