# BFS traversal to find all connected land components and check if total sum is divisible by k.
from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = grid[r][c]
                    grid[r][c] = 0
                    q = deque([(r, c)])

                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                q.append((nr, nc))

                    if island_sum % k == 0:
                        ans += 1

        return ans