'''
Given the head of a singly linked list, return true if it is a palindrome.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TmpUtil:
    @staticmethod
    def printLinkedList(ll: ListNode):
        while ll != None:
            print(ll.val, end=' ')
            ll = ll.next
        print()

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
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        outputList = ListNode(head.val)
        head = head.next
        while head != None:
            outputList = ListNode(head.val, outputList)
            head = head.next
        return outputList

    def isPalindrome_v1(self, head: ListNode) -> bool:
        oStr = ''
        rStr = ''
        while head != None:
            oStr += str(head.val)
            rStr = str(head.val) + rStr
            head = head.next
        return oStr == rStr

    def isPalindrome_v2(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        ## Find cutNode
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        ## Reverse the slow list
        slow = self.reverseList(slow)

        ## Compare the reversed slow list and the origin head
        while slow != None:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True

if __name__ == "__main__":
    sol = Solution()
    l = sol.list2LinkedList([1,2])
    TmpUtil.printLinkedList(sol.reverseList(l))
