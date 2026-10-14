class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum is greater than the maximum possible sum with 'num' digits
        if sum > 9 * num:
            return ""
        
        # Count how many 9s we can use
        count_9 = sum // 9
        # Find the single remainder digit
        rem = sum % 9
        
        # Count the number of 0s needed to pad to exactly 'num' digits
        count_0 = num - count_9 - (1 if rem > 0 else 0)
        
        # Construct the maximum number by placing larger digits first
        if rem > 0:
            return "9" * count_9 + str(rem) + "0" * count_0
        else:
            return "9" * count_9 + "0" * count_0
