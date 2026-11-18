import functools

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(None)
        def dp(i: int, j: int) -> bool:
            # If pattern pointer reaches the end, string pointer must also reach the end
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If the next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Choice 1: Skip '*' and preceding element (0 occurrences)
                # Choice 2: Use '*' to match current char and stay on pattern (1 or more occurrences)
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Normal match, advance both pointers
                return first_match and dp(i + 1, j + 1)
                
        return dp(0, 0)