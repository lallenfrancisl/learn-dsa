from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        els = set(nums)

        return len(els) != len(nums)
