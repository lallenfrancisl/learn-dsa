from typing import Optional

from tree_node import TreeNode


class Solution:
    MAX_LIMIT = 2**31
    MIN_LIMIT = -(2**31) - 1

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self._validate(root, Solution.MIN_LIMIT, Solution.MAX_LIMIT)

    def _validate(
        self,
        node: TreeNode | None,
        lower: int,
        upper: int,
    ) -> bool:
        if not node:
            return True

        if not (lower < node.val and node.val < upper):
            return False

        return self._validate(
            node.left,
            lower,
            node.val,
        ) and self._validate(node.right, node.val, upper)
