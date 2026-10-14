class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Travel each slot and its a 1:
        DFS and convert every 1 to a 0, and islands++
        """
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                # checks for boundaries and if it touches a water slot.
                return
            else:
                # mark as visited
                grid[r][c] = '0'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands


