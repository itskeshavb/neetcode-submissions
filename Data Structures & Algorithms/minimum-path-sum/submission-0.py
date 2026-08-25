class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[float('inf') for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for r in range(row):
            for c in range(col):
                if r>0:
                    dp[r][c] = min(dp[r][c], dp[r-1][c]+grid[r][c])
                if c>0:
                    dp[r][c]=min(dp[r][c], dp[r][c-1]+grid[r][c])
        return dp[row-1][col-1]