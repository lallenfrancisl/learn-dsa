class Solution:
    def maxArea(self, heights: list[int]) -> int:
        largest = 0

        l_ptr = 0
        r_ptr = len(heights) - 1
        while l_ptr < r_ptr:
            area = (r_ptr - l_ptr) * min(heights[l_ptr], heights[r_ptr])
            largest = max(area, largest)

            if heights[l_ptr] < heights[r_ptr]:
                l_ptr += 1
            else:
                r_ptr -= 1

        return largest
