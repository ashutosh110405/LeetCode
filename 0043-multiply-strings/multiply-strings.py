class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        
        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Current sum at p2 plus the multiplication result
                total = mul + pos[p2]
                
                # Store carry in p1 and remainder in p2
                pos[p2] = total % 10
                pos[p1] += total // 10
                
        # Convert the result array to a string and strip leading zeros
        result_str = "".join(map(str, pos))
        return result_str.lstrip("0")