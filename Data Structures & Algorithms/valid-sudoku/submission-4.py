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
        for start_x in range(0,9,3):
            for start_y in range(0,9,3):
                box_check = set()
                for row in range(start_x,start_x+3):
                    for col in range(start_y,start_y+3):
                        curr = board[row][col]
                        if curr == '.':
                            continue
                        if curr in row_check[row]:
                            print('row', curr, row, row_check[row])
                            return False
                        else:
                            row_check[row].add(curr)
                        if curr in col_check[col]:
                            print('col', curr, col, col_check[col])
                            return False
                        else:
                            col_check[col].add(curr)
                        if curr in box_check:
                            print('box', curr, box_check)
                            return False
                        else:
                            box_check.add(curr)
        
        return True
