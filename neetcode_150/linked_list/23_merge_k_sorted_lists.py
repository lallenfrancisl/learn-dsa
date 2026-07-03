from typing import Optional

from list_node import ListNode


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists: list[ListNode | None] = []

            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                list_2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(self.merge_lists(list_1, list_2))

            lists = merged_lists

        return lists[0]

    def merge_lists(self, list_1: ListNode | None, list_2: ListNode | None):
        dummy = ListNode()
        tail = dummy

        while list_1 is not None and list_2 is not None:
            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next

            tail = tail.next

        if list_1 is not None:
            tail.next = list_1

        if list_2 is not None:
            tail.next = list_2

        return dummy.next
