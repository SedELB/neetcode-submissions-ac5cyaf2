class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        areas = []
        def dfs(r, c):
            if (0 <= r < rows) and (0 <= c < cols) and (grid[r][c] == 1):
                nonlocal area
                grid[r][c] = 0 # mark it as visited
                area += 1

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    areas.append(area)
        
        return max(areas) if areas else 0

