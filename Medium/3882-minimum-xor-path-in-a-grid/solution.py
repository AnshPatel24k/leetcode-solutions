# Approach:
# We can use dynamic programming with sets to track all possible path XOR values reaching cell (i, j).
# Since m * n <= 1000 and cell values are <= 1023, the maximum XOR value is <= 1023.
# For each cell, we take the union of valid path XORs from the top and left adjacent cells and XOR each with grid[i][j].

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0] = {grid[0][0]}
                    continue
                
                prev = set()
                if i > 0:
                    prev.update(dp[j])
                if j > 0:
                    prev.update(dp[j - 1])
                
                val = grid[i][j]
                dp[j] = {x ^ val for x in prev}
                
        return min(dp[-1])