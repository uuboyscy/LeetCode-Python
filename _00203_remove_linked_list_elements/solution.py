"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""
from __future__ import annotations
import sys; sys.path.append("./")
from generalUtil.LinkedListUtil import list2LinkedList, printLinkedList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if not head:
            return head

        while head.val == val and head.next:
            head = head.next

        current_head = head
        check_point_head = None
        has_skipped = False
        while current_head.next:
            if current_head.val == val:
                has_skipped = True
            else:
                if has_skipped:
                    check_point_head.next = current_head
                check_point_head = current_head
                has_skipped = False
            current_head = current_head.next

        if check_point_head:
            check_point_head.next = None if current_head.val == val else current_head

        if head.val == val:
            return None

        return head

if __name__ == "__main__":
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    printLinkedList(Solution().removeElements(list2LinkedList(head), val))

    print("+++++")

    head = []
    val = 1
    printLinkedList(Solution().removeElements(list2LinkedList(head), val))

    print("+++++")

    head = [7, 7, 7, 7]
    val = 7
    printLinkedList(Solution().removeElements(list2LinkedList(head), val))

    print("+++++")

    head = [1]
    val = 1
    printLinkedList(Solution().removeElements(list2LinkedList(head), val))

    print("+++++")

    head = [1,2]
    val = 1
    printLinkedList(Solution().removeElements(list2LinkedList(head), val))

    print("+++++")

    head = [1,2,2,1]
    val = 2
    printLinkedList(Solution().removeElements(list2LinkedList(head), val))

    print("+++++")