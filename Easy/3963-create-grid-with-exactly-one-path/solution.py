# Approach: Create an L-shaped path of free cells '.' along column 0 and row m-1,
# placing obstacles '#' everywhere else. This guarantees a single unique path
# from (0, 0) down to (m-1, 0) and then right to (m-1, n-1).

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return [
            "".join('.' if i == m - 1 or j == 0 else '#' for j in range(n))
            for i in range(m)
        ]