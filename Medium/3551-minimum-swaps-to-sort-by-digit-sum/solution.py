class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to get the sum of digits
        def digit_sum(x: int) -> int:
            return sum(map(int, str(x)))
        
        # Store (digit_sum, val, original_index)
        arr = [(digit_sum(x), x, i) for i, x in enumerate(nums)]
        
        # Sort based on digit_sum first, then value
        arr.sort()
        
        # Map original_index -> target_index
        target_pos = [0] * n
        for target_idx, (_, _, orig_idx) in enumerate(arr):
            target_pos[orig_idx] = target_idx
            
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or target_pos[i] == i:
                continue
            
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_pos[curr]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += cycle_size - 1
                
        return swaps