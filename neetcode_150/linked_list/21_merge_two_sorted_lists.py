from typing import Optional

from list_node import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head: ListNode | None = None

        left = list1
        right = list2

        if left is None:
            return right

        if right is None:
            return left

        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next

        cur = head
        while left is not None or right is not None:
            if left is not None and right is not None:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
            elif left is None and right is not None:
                cur.next = right
                right = right.next
            elif left is not None and right is None:
                cur.next = left
                left = left.next
            else:
                continue

            cur = cur.next

        return head
