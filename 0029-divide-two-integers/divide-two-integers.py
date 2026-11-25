class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647

        # Handle 32-bit signed integer overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp = b
            multiple = 1
            while (temp << 1) <= a:
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple

        return -quotient if negative else quotient