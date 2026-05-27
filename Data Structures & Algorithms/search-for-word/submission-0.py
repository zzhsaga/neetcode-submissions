class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # create direction list
        # for each position
        # we check if nxt step is valid
        # 1. boudary
        # 2. if visited(I dont think this would make sense, think about path CCAT.we have to start with the second C to continue )
        # 3. align with target word
        # 2 is gone, one problem is should be do it seperately or tegother, ussually checking boundary first before access is valid, but place them seperate might increase complexity
        # okay, visited is nessaray since it cant go back to where it comes from
        def check(row,col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row,col) in visited:
                return False
            return True
        def dfs(row,col,curr):
            a = ""
            for v in visited:
                a += board[v[0]][v[1]]
            # print(a,row,col,curr)
            if not check(row,col) or board[row][col] != word[curr] or self.ans:
                return 
            
            visited.append((row,col))
            if curr == len(word) - 1:
                self.ans = True
                return
            for r,c in direction:
                dfs(row+r,col+c,curr+1)
            visited.pop()
        visited = []
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        self.ans = False
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x,y,0)

        return self.ans

