class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r =  0, len(matrix) - 1
        matrixInd = None

        while l <= r:
            mid = ((r - l) // 2) + l
            if matrix[mid][0] <= target:
                if matrix[mid][len(matrix[mid]) - 1] >= target:
                    matrixInd = mid
                    break
                else:
                    l = mid + 1
            else:
                r = mid - 1
        
        if matrixInd is None:
            return False
        
        l, r = 0, len(matrix[matrixInd]) - 1

        while l <= r:
            mid = ((r - l) // 2) + l
            if matrix[matrixInd][mid] == target:
                return True
            if matrix[matrixInd][mid] > target:
                r = mid - 1
            else:
                l =  mid + 1
        return False

        
                