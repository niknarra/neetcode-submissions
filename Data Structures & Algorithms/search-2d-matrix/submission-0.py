class Solution:
    def binSearch(self, row, target):
        low = 0
        high = len(row) - 1

        while low <= high:
            mid = (low + high)//2

            if row[mid] == target:
                return True
            
            elif row[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, top = 0, 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        low = matrix[0][0]
        high = matrix[0][len(matrix[0])-1]

        while top <= bottom:
            if matrix[top][left] <= target <= matrix[top][right]:
                return self.binSearch(matrix[top], target)

            top += 1

        return False
