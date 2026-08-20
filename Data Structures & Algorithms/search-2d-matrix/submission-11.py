class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        index = -1
        while l <= r:
            m = (l+r) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                index = m
                break
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        if index == -1:
            return False
        l, r = 0, len(matrix[index])

        while l <= r:
            m = (l+r) // 2
            if matrix[index][m] == target:
                return True
            if matrix[index][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False