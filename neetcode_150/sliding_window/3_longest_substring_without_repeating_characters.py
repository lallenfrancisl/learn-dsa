from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0

        visited: Set[str] = set()
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])
            length = max(length, right - left + 1)

        return length
