from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False

        return self.val == other.val and self.next is other.next

    def to_list(self) -> list[int]:
        values = []
        current: ListNode | None = self

        while current is not None:
            values.append(current.val)
            current = current.next

        return values

    def __str__(self) -> str:
        return f"[{', '.join(map(lambda x: str(x), self.to_list()))}]"

    def __repr__(self) -> str:
        return self.__str__()


def to_list_node(values: list[int]) -> ListNode | None:
    head: ListNode | None = None

    for value in reversed(values):
        head = ListNode(value, head)

    return head
