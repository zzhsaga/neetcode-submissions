class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]

        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                block_check = set()
                for m in range(3):
                    for n in range(3):
                        row = i + m
                        col = j + n
                        curr = board[row][col]
                        if curr == '.':
                            continue 
                        if curr in block_check or curr in row_check[i+m] or curr in col_check[j+n]:
                            return False
                        else:
                            block_check.add(curr)
                            row_check[row].add(curr)
                            col_check[col].add(curr)


        return True
        