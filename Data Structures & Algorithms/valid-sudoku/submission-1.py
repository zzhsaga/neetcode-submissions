class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]

        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                block_check = set()
                for m in range(3):
                    for n in range(3):
                        curr = board[i+m][j+n]
                        if curr == '.':
                            continue 
                        if curr in block_check:
                            return False
                        else:
                            block_check.add(curr)
                        if curr in row_check[i+m]:
                            return False
                        else:
                            row_check[i+m].add(curr)
                        if curr in col_check[j+n]:
                            return False
                        else:
                            col_check[j+n].add(curr)

        return True
        