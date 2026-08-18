class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        matrixI = None

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target:
                if matrix[m][-1] >= target:
                    matrixI = m
                    break
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        if matrixI is None:
            return False
        
        l, r = 0, len(matrix[matrixI]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[matrixI][m] == target:
                return True
            if matrix[matrixI][m] >= target:
                r = m - 1
            else:
                l = m + 1
        
        return False


        
                