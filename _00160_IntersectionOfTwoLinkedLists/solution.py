class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 != None else headB
            l2 = l2.next if l2 != None else headA

        return l1

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB
        cA = 0
        cB = 0

        while l1 != None:
            l1 = l1.next
            cA += 1
        while l2 != None:
            l2 = l2.next
            cB += 1

        if cA > cB:
            for i in range(0, cA - cB):
                headA = headA.next
            while headA != headB:
                headA = headA.next
                headB = headB.next
        else:
            for i in range(0, cB - cA):
                headB = headB.next
            while headA != headB:
                headA = headA.next
                headB = headB.next
        return headA

if __name__ == '__main__':
    sol = Solution()
    intersecList = [1, 8, 4, 5]
    l1 = [4] + intersecList
    l2 = [5, 6] + intersecList
    print(TmpUtil.list2LinkedList(l1).val)
    print(TmpUtil.list2LinkedList(l1).next.val)
    print(TmpUtil.list2LinkedList(l1).next.next.val)
    print(TmpUtil.list2LinkedList(l1).next.next.next.val)
    print(TmpUtil.list2LinkedList(l1).next.next.next.next.val)
    print(TmpUtil.list2LinkedList(l1).next.next.next.next.next)
    print(TmpUtil.list2LinkedList(l1).next.val == TmpUtil.list2LinkedList(l2).next.next.val)
    print(TmpUtil.list2LinkedList(l1).next == TmpUtil.list2LinkedList(l2).next.next)
    print(sol.getIntersectionNode(TmpUtil.list2LinkedList(l1), TmpUtil.list2LinkedList(l2)))

