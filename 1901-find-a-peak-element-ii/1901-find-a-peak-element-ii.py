class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            row = max(range(n), key=lambda i: mat[i][mid])
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1
            if mat[row][mid] > left and mat[row][mid] > right: 
                return [row, mid]
            elif mat[row][mid] < right:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]



        