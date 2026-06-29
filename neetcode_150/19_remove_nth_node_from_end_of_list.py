from typing import Optional, Tuple

from list_node import ListNode


class SolutionRecursive:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        _, new_head = self._remove(head, n)

        return new_head

    def _remove(
        self, head: ListNode | None, remove_at: int
    ) -> Tuple[int, ListNode | None]:
        if head is None:
            return (0, None)

        next_node_pos, next_node = self._remove(head.next, remove_at)
        head.next = next_node
        count_from_last = 1 + next_node_pos

        if count_from_last == remove_at:
            return (count_from_last, next_node)

        return (count_from_last, head)


class SolutionLooped:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
