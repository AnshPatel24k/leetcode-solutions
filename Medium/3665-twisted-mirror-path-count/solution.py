class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # If the start or end cell itself is invalid/out of bounds, no paths exist
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        memo = {}

        def get_next_cell(r, c, direction):
            """
            Simulates the movement from (r, c) in the given direction 
            until it hits an empty cell (0) or goes out of bounds.
            """
            curr_r, curr_c = r, c
            
            # Take the initial step
            if direction == 'Right':
                curr_c += 1
            else:
                curr_r += 1
                
            # Follow reflections if hitting mirrors (1)
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                if direction == 'Right':
                    curr_r += 1
                    direction = 'Down'
                else:
                    curr_c += 1
                    direction = 'Right'
            
            # Check if final resting position is within bounds
            if 0 <= curr_r < m and 0 <= curr_c < n:
                return (curr_r, curr_c)
            return None

        def dfs(r, c):
            # Base Case: Reached the destination
            if r == m - 1 and c == n - 1:
                return 1
                
            if (r, c) in memo:
                return memo[(r, c)]
            
            total_paths = 0
            
            # Option 1: Move Right
            next_right = get_next_cell(r, c, 'Right')
            if next_right:
                total_paths = (total_paths + dfs(next_right[0], next_right[1])) % MOD
                
            # Option 2: Move Down
            next_down = get_next_cell(r, c, 'Down')
            if next_down:
                total_paths = (total_paths + dfs(next_down[0], next_down[1])) % MOD
                
            memo[(r, c)] = total_paths
            return total_paths

        return dfs(0, 0)

