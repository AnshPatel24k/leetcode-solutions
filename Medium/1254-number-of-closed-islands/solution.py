class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            grid[r][c] = 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    dfs(nr, nc)

        # Eliminate land connected to boundaries
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and grid[r][c] == 0:
                    dfs(r, c)

        # Count remaining closed islands
        closed_islands = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c)

        return closed_islands