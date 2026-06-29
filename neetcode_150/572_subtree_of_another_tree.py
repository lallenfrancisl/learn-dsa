from typing import Optional

from tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if sub_root is None:
            return True

        if root is None:
            return False

        if self.is_same(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(
            root.right, sub_root
        )

    def is_same(self, s: TreeNode | None, t: TreeNode | None):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return self.is_same(s.left, t.left) and self.is_same(s.right, t.right)

        return False
