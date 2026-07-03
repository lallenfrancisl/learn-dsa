from typing import Optional

from list_node import ListNode


class SolutionRecursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        reversed = self._reverse(None, head)

        return reversed

    def _reverse(self, prev: ListNode | None, curr: ListNode) -> ListNode:
        if curr.next is None:
            curr.next = prev

            return curr

        head = self._reverse(curr, curr.next)
        curr.next = prev

        return head


class SolutionLooped:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
