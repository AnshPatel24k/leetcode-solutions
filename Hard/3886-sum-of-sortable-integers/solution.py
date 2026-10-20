class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        def is_valid(k: int) -> bool:
            # Check each consecutive subarray of length k
            for i in range(0, n, k):
                block = nums[i:i+k]
                drop_count = 0
                drop_idx = -1
                
                # Count cyclic drops within the block
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drop_count += 1
                        drop_idx = j
                        if drop_count > 1:
                            return False
                
                # Reconstruct the sorted block based on the drop index
                if drop_count == 1:
                    reconstructed = block[drop_idx + 1:] + block[:drop_idx + 1]
                else:
                    reconstructed = block
                
                # Check if it matches the corresponding segment of the sorted array
                if reconstructed != sorted_nums[i:i+k]:
                    return False
                    
            return True

        ans = 0
        # Find and test all divisors of n
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                if is_valid(k):
                    ans += k
                if k * k != n:
                    if is_valid(n // k):
                        ans += n // k
                        
        return ans
