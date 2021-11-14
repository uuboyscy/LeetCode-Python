'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def list2LinkedList(inputList: list) -> ListNode:
        outputLinkedList = None
        tmpLinkedList = None
        for n, i in enumerate(inputList[::-1]):
            outputLinkedList = ListNode(i)
            outputLinkedList.next = tmpLinkedList
            tmpLinkedList = outputLinkedList

        return outputLinkedList

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmpList = list()
        while head != None:
            tmpList.append(head.val)
            head = head.next
        targetIndex = tmpList.__len__() - n
        newList = [i for m, i in enumerate(tmpList) if m != targetIndex]
        return self.list2LinkedList(newList)

if __name__ == '__main__':
    sol = Solution()
    s = [0, 1, 2, 3]
