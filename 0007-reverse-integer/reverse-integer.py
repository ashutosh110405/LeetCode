class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        # Track whether the number is negative
        negative = x < 0
        x = abs(x)
        
        res = 0
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before updating `res`
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
                return 0
                
            res = res * 10 + pop
            
        return -res if negative else res