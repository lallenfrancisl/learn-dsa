from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)

        longest = 0
        for i in lookup:
            if (i - 1) not in lookup:
                streak = 1
                curr = i

                while (curr + 1) in lookup:
                    streak += 1
                    curr += 1

                longest = max(longest, streak)

        return longest
