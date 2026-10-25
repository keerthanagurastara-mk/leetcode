class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])

            length = i - left + 1

            if length > max_length:
                max_length = length

        return max_length