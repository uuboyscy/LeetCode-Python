'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TmpUtil:
    @staticmethod
    def list2LinkedList(inputList: list) -> ListNode:
        outputLinkedList = None
        tmpLinkedList = None
        for n, i in enumerate(inputList[::-1]):
            if n == 0:
                tmpLinkedList = ListNode(i)
            else:
                outputLinkedList = ListNode(i)
                outputLinkedList.next = tmpLinkedList
                tmpLinkedList = outputLinkedList

        return outputLinkedList

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        outputListNode = None
        while head != None:
            outputListNode = ListNode(head.val, outputListNode)
            head = head.next
        return outputListNode

if __name__ == '__main__':
    sol = Solution()
    intersecList = [1, 8, 4, 5]
    l1 = [4] + intersecList
    l2 = [5, 6] + intersecList
    a = sol.reverseList(TmpUtil.list2LinkedList(intersecList))
    print(a.val)
    print(a.next.val)
    print(a.next.next.val)
    print(a.next.next.next.val)
    print(a.next.next.next.next)


