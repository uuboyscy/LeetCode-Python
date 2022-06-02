"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

"""
Runtime: 65 ms, faster than 53.93% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.2 MB, less than 85.03% of Python3 online submissions for Reverse Nodes in k-Group.
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

        # Initiation
        outputHead = head
        tmpStartHead = head
        kArray = list()
        i = 0

        while head != None:
            if i < k:
                kArray.append(head.val)
                head = head.next
                i += 1
            else:
                kArray.reverse()
                for nodeVal in kArray:
                    tmpStartHead.val = nodeVal
                    tmpStartHead = tmpStartHead.next
                kArray = list()
                # tmpStartHead = head
                i = 0

        if i == k:
            kArray.reverse()
            for nodeVal in kArray:
                tmpStartHead.val = nodeVal
                tmpStartHead = tmpStartHead.next

        return outputHead


if __name__ == '__main__':
    s = Solution()

