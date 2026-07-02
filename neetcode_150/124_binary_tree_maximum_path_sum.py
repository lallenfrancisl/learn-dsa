from typing import Optional

from tree_node import TreeNode


class Solution:
    MIN_SUM = -(3 * 10**7)

    def __init__(self) -> None:
        self.max_sum = self.MIN_SUM

    def maxPathSum(self, root: TreeNode | None) -> int:
        self._max_node_sum(root)

        return self.max_sum

    def _max_node_sum(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_max = max(
            0,
            self._max_node_sum(
                node.left,
            ),
        )
        right_max = max(
            0,
            self._max_node_sum(
                node.right,
            ),
        )

        self.max_sum = max(self.max_sum, node.val + left_max + right_max)

        return node.val + max(left_max, right_max)
