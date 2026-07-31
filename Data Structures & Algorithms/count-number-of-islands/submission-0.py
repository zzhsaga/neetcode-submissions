class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # def bfs(r,c):
        #     deq = deque([(r,c)])
        #     while deq:
        #         r,c = deq.popleft()
        #         if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
        #             grid[r][c] = '0'
        #             for dx, dy in directions:
        #                 deq.append((r+dx,c+dy))

        def dfs(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = '0'
                for dx, dy in directions:
                    dfs(r+dx,c+dy)


        directions  = [(0,1),(1,0),(0,-1),(-1,0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        
        if not grid:
            return 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row,col)
                    islands += 1
        
        return islands
