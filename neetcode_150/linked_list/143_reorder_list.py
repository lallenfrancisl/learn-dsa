from typing import Optional

from list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> ListNode | None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev: ListNode | None = None
        slow.next = None

        # reversing the second part of the linked list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        second = prev
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        return head
