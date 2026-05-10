class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. search rows, find the row that first ele smaller than the target
        # 2. search the col, find the target
        # 3. it's logm + logn = log(mn)
        t = 0
        d = len(matrix) - 1

        while t < d:
            mid = (t+d+1)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                t = mid
            else:
                d = mid - 1
        
        l = 0
        r = len(matrix[t]) - 1
        row = matrix[t]

        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l += 1
            else:
                r -= 1

        return False