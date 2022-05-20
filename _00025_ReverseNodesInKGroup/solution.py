"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def list2LinkedList(inputList: list) -> ListNode:
            outputLinkedList = None
            tmpLinkedList = None
            if inputList == None or inputList.__len__() == 0:
                return None
            elif inputList.__len__() == 1:
                return ListNode(val=inputList[0])
            for n, i in enumerate(inputList[::-1]):
                if n == 0:
                    tmpLinkedList = ListNode(i)
                else:
                    outputLinkedList = ListNode(i)
                    outputLinkedList.next = tmpLinkedList
                    tmpLinkedList = outputLinkedList

            return outputLinkedList

        if head == None:
            return None
        outputListNode = None
        outputList = list()

        i = 0
        while i < k:
            if head == None:
                break
            outputList.append(head.val)
            head = head.next
            i += 1

        if i == k - 1:
            outputListNode = list2LinkedList(outputList.reverse())
            outputListNode.next = self.reverseKGroup(head, k)
            return outputListNode
        else:
            return list2LinkedList(outputList)


if __name__ == '__main__':
    s = Solution()

