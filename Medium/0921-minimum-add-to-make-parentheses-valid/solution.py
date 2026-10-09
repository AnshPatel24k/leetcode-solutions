class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0  # Tracks unmatched '(' that need a ')'
        close_needed = 0 # Tracks unmatched ')' that need a '('
        
        for char in s:
            if char == '(':
                # We found an open parenthesis, it needs a matching close parenthesis later
                close_needed += 1
            else:  # char == ')'
                if close_needed > 0:
                    # This ')' successfully matches a previous '('
                    close_needed -= 1
                else:
                    # No unmatched '(' is available, so we must add a '(' before this
                    open_needed += 1
                    
        # The total moves required is the sum of all unmatched parentheses
        return open_needed + close_needed
