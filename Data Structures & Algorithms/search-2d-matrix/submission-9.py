class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        i = None
        while l <= r:
            m = ((l+r) // 2) 
            if matrix[m][0] <= target:
                if matrix[m][-1] >= target:
                    i = m
                    break
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        if i is None:
            return False     
            
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            m = ((l+r) // 2) 
            if matrix[i][m] == target:
                return True
            if matrix[i][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False

        
                