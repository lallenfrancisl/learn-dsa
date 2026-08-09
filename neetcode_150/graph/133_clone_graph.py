# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None

        old_to_new: dict[Node, Node] = {}
        stack: list[Node] = [node]
        while stack:
            cur = stack.pop()
            old_to_new[cur] = Node(cur.val)

            for nbr in cur.neighbors:
                if nbr not in old_to_new:
                    stack.append(nbr)

        for old_n, new_n in old_to_new.items():
            for nei in old_n.neighbors:
                new_n.neighbors.append(old_to_new[nei])

        return old_to_new[node]
