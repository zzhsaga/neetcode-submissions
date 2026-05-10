class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for each, we need
        # 1. row check
        # 2. col check
        # 3. box check
        # box check is not natural if we check it indepdently, 
        # we need to create 9 check sets and identify the curr node belong to which
        # instead, we can simplfy this by loop box by box, so we only need to maintain one box checking set
        row_check = [set() for _ in range(len(board))]
        col_check = [set() for _ in range(len(board[0]))]
        box_check = [set() for _ in range(len(board[0])//3*len(board)//3)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                curr = board[row][col]
                if curr == ".":
                    continue
                box_id = 3*(row//3) + col//3
                if (curr in row_check[row] or
                    curr in col_check[col] or
                    curr in box_check[box_id]):
                    return False
                        
                row_check[row].add(curr)
                col_check[col].add(curr)
                box_check[box_id].add(curr)

        return True
