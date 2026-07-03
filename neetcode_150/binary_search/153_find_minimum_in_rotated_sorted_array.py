class Solution:
    def findMin(self, arr: list[int]) -> int:
        l_ptr = 0
        r_ptr = len(arr) - 1

        while l_ptr < r_ptr:
            mid_ptr = (l_ptr + r_ptr) // 2

            if arr[mid_ptr] > arr[r_ptr]:
                l_ptr = mid_ptr + 1
            else:
                r_ptr = mid_ptr

        return arr[l_ptr]
