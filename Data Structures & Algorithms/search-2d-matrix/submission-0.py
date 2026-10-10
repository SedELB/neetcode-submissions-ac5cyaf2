class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        target = 12
        [[1,2,4,8],
        [10,11,12,13],
        [14,20,30,40]]
        """ 
        # Check boundaries if target can be here.
        rows, cols = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False
        
        # Check each row if our target is comprised in each array.
        target_row = 0
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                target_row = i
                break
        
        
        # Now that we've found our target row, apply binary search on the row.
        low = 0
        high = len(matrix[target_row]) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if matrix[target_row][mid] == target:
                return True
            
            if matrix[target_row][mid] < target:
                low = mid + 1
            
            if matrix[target_row][mid] > target:
                high = mid - 1
        
        return False





            



