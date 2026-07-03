from typing import Tuple

from tree_node import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string."""

        return self._serialize(root, "")

    def _serialize(self, root: TreeNode | None, result: str) -> str:
        if len(result):
            result += ","

        if not root:
            return result + "N"

        result += f"{root.val}"
        result = self._serialize(root.left, result)
        result = self._serialize(root.right, result)

        return result

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree."""
        parts = data.split(",")
        if not parts:
            return None

        _, node = self._deserialize(parts, 0)

        return node

    def _deserialize(self, parts: list[str], ptr: int) -> Tuple[int, TreeNode | None]:
        cur = parts[ptr]
        if cur == "N":
            return (ptr + 1, None)

        node = TreeNode(int(cur))
        ptr += 1

        ptr, node.left = self._deserialize(parts, ptr)
        ptr, node.right = self._deserialize(parts, ptr)

        return (ptr, node)
