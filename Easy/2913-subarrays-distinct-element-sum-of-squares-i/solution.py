class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Iterate over all possible starting positions of the subarray
        for i in range(n):
            distinct_elements = set()
            
            # Iterate over all possible ending positions of the subarray
            for j in range(i, n):
                # Add the current element to the set to automatically track uniqueness
                distinct_elements.add(nums[j])
                
                # Calculate the distinct count squared and add to total
                distinct_count = len(distinct_elements)
                total_sum += distinct_count ** 2
                
        return total_sum
