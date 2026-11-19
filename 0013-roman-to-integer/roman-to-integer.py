class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        for i in range(len(s) - 1):
            curr_val = roman_map[s[i]]
            next_val = roman_map[s[i + 1]]
            if curr_val < next_val:
                total -= curr_val
            else:
                total += curr_val

        return total + roman_map[s[-1]]