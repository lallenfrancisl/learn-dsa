from collections import deque
from typing import Optional

from tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        stack = deque[TreeNode]([])
        cur = root
        result: list[int] = []

        while cur or stack and len(result) < k:
            if not cur:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right

                continue

            stack.append(cur)
            cur = cur.left

        return result.pop()
