class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l_ptr = i + 1
            r_ptr = len(nums) - 1

            while l_ptr < r_ptr:
                sum = a + nums[l_ptr] + nums[r_ptr]

                if sum == 0:
                    res.append([a, nums[l_ptr], nums[r_ptr]])
                    l_ptr += 1

                    while nums[l_ptr] == nums[l_ptr - 1] and l_ptr < r_ptr:
                        l_ptr += 1
                elif sum > 0:
                    r_ptr -= 1
                else:
                    l_ptr += 1

        return res
