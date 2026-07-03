from typing import Optional

from tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid + 1])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
