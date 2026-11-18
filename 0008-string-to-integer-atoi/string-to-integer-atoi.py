class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        # Step 2: Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3 & 4: Convert digits and handle clamping
        res = 0
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            # Check for overflow before updating `res`
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            res = res * 10 + digit
            i += 1
            
        return sign * res