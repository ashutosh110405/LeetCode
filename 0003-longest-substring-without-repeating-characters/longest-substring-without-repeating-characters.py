# class Solution:

#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_index_map = {}
#         max_length = 0
#         left = 0

#         for right in range(len(s)):
#             char = s[right]

#             # If character is seen and is within the current window, move the left pointer
#             if char in char_index_map and char_index_map[char] >= left:
#                 left = char_index_map[char] + 1

#             # Update the character's latest index
#             char_index_map[char] = right

#             # Calculate the maximum length of the substring without repeating characters
#             max_length = max(max_length, right - left + 1)

#         return max_length


# # Example usage:
# sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
# print(sol.lengthOfLongestSubstring("bbbbb"))  # Output: 1 ("b")
# print(sol.lengthOfLongestSubstring("pwwkew"))  # Output: 3 ("wke")





class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0

        for i in range(len(s)):
            temp = ""

            for j in range(i, len(s)):
                ch = s[j]

                if ch not in temp:
                    temp += ch
                else:
                    break

            if len(temp) > max_len:
                max_len = len(temp)

        return max_len