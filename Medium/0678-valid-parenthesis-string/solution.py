class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimum possible open '('
        cmax = 0  # Maximum possible open '('
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmin -= 1
                cmax += 1
                
            # If maximum possible open parentheses drops below 0, it's invalid
            if cmax < 0:
                return False
            
            # cmin cannot be less than 0
            if cmin < 0:
                cmin = 0
                
        # If minimum possible open parentheses is 0, the string is valid
        return cmin == 0
