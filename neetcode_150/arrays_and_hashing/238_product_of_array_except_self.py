from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = []

        pre = 1
        for i, val in enumerate(nums):
            result.append(pre)
            pre = pre * val

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * post
            post = post * nums[i]

        return result
