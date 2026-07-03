from collections import deque
from typing import Optional

from tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels: list[list[int]] = []

        queue = deque([root])
        while queue:
            size = len(queue)
            level: list[int] = []

            for _ in range(size):
                node = queue.popleft()

                if node is not None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                levels.append(level)

        return levels
