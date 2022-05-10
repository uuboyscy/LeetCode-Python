# """
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
# """
#
# from typing import Optional
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class TmpUtil:
#     @staticmethod
#     def list2LinkedList(inputList: list) -> ListNode:
#         outputLinkedList = None
#         tmpLinkedList = None
#         for n, i in enumerate(inputList[::-1]):
#             if n == 0:
#                 tmpLinkedList = ListNode(i)
#             else:
#                 outputLinkedList = ListNode(i)
#                 outputLinkedList.next = tmpLinkedList
#                 tmpLinkedList = outputLinkedList
#
#         return outputLinkedList
#
#     @staticmethod
#     def printLinkedList(ll: ListNode):
#         while ll != None:
#             print(ll.val, end=' ')
#             ll = ll.next
#         print()
#
#     @staticmethod
#     def linkedList2List(inputLinkedList: ListNode) -> list:
#         outputList = list()
#         while inputLinkedList != None:
#             outputList.append(inputLinkedList.val)
#             inputLinkedList = inputLinkedList.next
#
#
# class Solution:
#     def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
#         def list2LinkedList(inputList: list) -> ListNode:
#             outputLinkedList = None
#             tmpLinkedList = None
#             for n, i in enumerate(inputList[::-1]):
#                 if n == 0:
#                     tmpLinkedList = ListNode(i)
#                 else:
#                     outputLinkedList = ListNode(i)
#                     outputLinkedList.next = tmpLinkedList
#                     tmpLinkedList = outputLinkedList
#
#             return outputLinkedList
#
#         outputList = list()
#         isAnyOneValid = False
#         # minNumber = -10e+4
#         maxNumber = 10e+4
#         if lists.__len__() > 0:
#             for ll in lists:
#                 if ll != None:
#                     isAnyOneValid = True
#                     break
#                 return ListNode()
#         else:
#             return ListNode()
#
#         tmpMinNumber = maxNumber
#         while isAnyOneValid:
#             tmpIdx = -1
#             isAnyOneValid = False
#             for idx, ll in enumerate(lists):
#                 if ll is None:
#                     continue
#                 else:
#                     isAnyOneValid = True
#                 if ll.val <= tmpMinNumber:
#                     tmpMinNumber = ll.val
#                     tmpIdx = idx
#             outputList.append(tmpMinNumber)
#             if isAnyOneValid and tmpIdx != -1:
#                 lists[tmpIdx] = lists[tmpIdx].next
#
#         return list2LinkedList(outputList)
#
#
# if __name__ == '__main__':
#     s = Solution()
#
#     inputLists = [[1,4,5],[1,3,4],[2,6]]
#
#
#     inputLists = []
#
#     inputLists = [[]]