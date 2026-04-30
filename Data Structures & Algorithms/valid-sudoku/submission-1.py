class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking rows for duplicates
        for row in board:
            if self.hasDuplicate(row):
                return False

        # checking cols for duplicates
        for i in range(len(board)):
            column = [row[i] for row in board]
            if self.hasDuplicate(column):
                return False
        
        start = 0
        col = 3
        for k in range(0, 9, 3): # 0, 3, 6
            start = 0
            col = 3

            for square in range(3):
                row = k
                arr1 = board[row][start:col] # board[0][0:2] board[1][0:2]
                row += 1

                arr2 = board[row][start:col]
                row += 1

                arr3 = board[row][start:col]
                row += 1

                arr = arr1+arr2+arr3
                if self.hasDuplicate(arr):
                    return False
                
                start += 3
                col = start + 3
        
        return True
            

    def hasDuplicate(self, arr):
        hashset = set()
        for elem in arr:
            if elem.isdigit():
                if elem in hashset:
                    return True
                else:
                    hashset.add(elem)
        
        return False

    
