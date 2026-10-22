from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Find the index of 0 in the current nums array
        idx0 = nums.index(0)
        
        target_r = -1
        target_s = -1
        
        # Check if the sorted state can be reached with r = 0 (no effective flip needed)
        # In this state, element i should be at nums[(s + i) % n]
        is_normal = True
        for i in range(n):
            if nums[(idx0 + i) % n] != i:
                is_normal = False
                break
        if is_normal:
            target_r = 0
            target_s = idx0
            
        # Check if the sorted state can be reached with r = 1 (flipped state)
        # In this state, element i should be at nums[(idx0 - i) % n]
        else:
            is_reversed = True
            for i in range(n):
                if nums[(idx0 - i) % n] != i:
                    is_reversed = False
                    break
            if is_reversed:
                target_r = 1
                target_s = (n - 1 - idx0) % n
                
        # If the array configuration doesn't match a valid cyclic shift, it's impossible
        if target_r == -1:
            return -1
            
        # Standard BFS to find the shortest path from (0, 0) to (target_r, target_s)
        dist = [[-1] * n for _ in range(2)]
        queue = deque([(0, 0)])
        dist[0][0] = 0
        
        while queue:
            r, s = queue.popleft()
            
            if r == target_r and s == target_s:
                return dist[r][s]
                
            # Transition 1: Rotate Left
            nr1, ns1 = r, (s + 1) % n
            if dist[nr1][ns1] == -1:
                dist[nr1][ns1] = dist[r][s] + 1
                queue.append((nr1, ns1))
                
            # Transition 2: Reverse
            nr2, ns2 = 1 - r, (n - s) % n
            if dist[nr2][ns2] == -1:
                dist[nr2][ns2] = dist[r][s] + 1
                queue.append((nr2, ns2))
                
        return -1
