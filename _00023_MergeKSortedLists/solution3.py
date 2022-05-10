"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
"""
Success
Details 
Runtime: 95 ms, faster than 97.07% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.6 MB, less than 14.28% of Python3 online submissions for Merge k Sorted Lists.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class TmpUtil:
    @staticmethod
    def list2LinkedList(inputList: list) -> ListNode:
        outputLinkedList = None
        tmpLinkedList = None
        if inputList.__len__() == 0:
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

    @staticmethod
    def printLinkedList(ll: ListNode):
        while ll != None:
            print(ll.val, end=' ')
            ll = ll.next
        print()

    @staticmethod
    def linkedList2List(inputLinkedList: ListNode) -> list:
        outputList = list()
        while inputLinkedList != None:
            outputList.append(inputLinkedList.val)
            inputLinkedList = inputLinkedList.next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        def list2LinkedList(inputList: list) -> ListNode:
            outputLinkedList = None
            tmpLinkedList = None
            if inputList.__len__() == 0:
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

        outputList = list()
        isAnyOneValid = False
        if lists.__len__() > 0:
            for ll in lists:
                if ll != None:
                    isAnyOneValid = True
                    break
        else:
            return None

        if isAnyOneValid:
            for ll in lists:
                while ll != None:
                    outputList.append(ll.val)
                    ll = ll.next
        else:
            return None

        return list2LinkedList(sorted(outputList))


if __name__ == '__main__':
    s = Solution()

    inputLists = [[1,4,5],[1,3,4],[2,6]]


    inputLists = []

    inputLists = [[]]

    ll = TmpUtil.list2LinkedList([1])
    TmpUtil.printLinkedList(ll)
    print(ll.val)