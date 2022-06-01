"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

"""
Runtime: 66 ms, faster than 51.87% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.8 MB, less than 7.43% of Python3 online submissions for Reverse Nodes in k-Group.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k <= 1:
            return head

        # Original Node
        backupHead = head

        # Create last node in this partial reversed node
        lastNode = ListNode(val=head.val)

        # Create first reversed node
        head = head.next
        if head == None:
            return backupHead
        outputListNode = ListNode(val=head.val, next=lastNode)

        i = 2
        while i < k:
            head = head.next
            if head == None:
                return backupHead
            outputListNode = ListNode(val=head.val, next=outputListNode)
            i += 1

        lastNode.next = self.reverseKGroup(head=head.next, k=k)

        return outputListNode


if __name__ == '__main__':
    s = Solution()

