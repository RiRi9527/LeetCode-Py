class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_index = {}
        start = 0
        maxLength = 0

        for index, char in enumerate(s):  
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = index
            maxLength = max(maxLength, index - start +1)

        return maxLength

s = Solution()
print(s.lengthOfLongestSubstring("aacdabbbb") )


# def length_of_longest_substring(s: str) -> int:
#     char_index_map = {}
#     longest = 0
#     start = 0

#     for i, char in enumerate(s):
#         if char in char_index_map and char_index_map[char] >= start:
#             start = char_index_map[char] + 1
#         char_index_map[char] = i
#         longest = max(longest, i - start + 1)

#     return longest

# # Example usage:
# s1 = "abcabcbb"
# s2 = "bbbbb"
# s3 = "pwwkew"

# print(length_of_longest_substring(s1))  # Output: 3
# print(length_of_longest_substring(s2))  # Output: 1
# print(length_of_longest_substring(s3))  # Output: 3