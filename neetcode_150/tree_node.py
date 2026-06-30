class TreeNode:
    def __init__(
        self, val=0, left: "TreeNode" | None = None, right: "TreeNode" | None = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        values = []
        level = [self]

        while any(level):
            values.extend(node.val if node else None for node in level)

            next_level = []
            for node in level:
                if node:
                    next_level.extend([node.left, node.right])
                else:
                    next_level.extend([None, None])

            while next_level and next_level[-1] is None:
                next_level.pop()

            level = next_level

        return str(values)
