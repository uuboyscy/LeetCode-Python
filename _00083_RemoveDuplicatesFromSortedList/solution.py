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

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        distinctList = list()
        tmpVal = head.val
        while head != None:
            head = head.next
            if head == None:
                pass
            elif head.val == tmpVal:
                continue
            distinctList.append(tmpVal)
            tmpVal = None if head == None else head.val
        return self.list2LinkedList(distinctList)

if __name__ == "__main__":
    sol = Solution()
    l1 = Solution.list2LinkedList([1,1,2,3,4,4,5,5])
    l11 = sol.deleteDuplicates(l1)
    TmpUtil.printLinkedList(l1)
    TmpUtil.printLinkedList(l11)

    print()

    l1 = Solution.list2LinkedList([1])
    l11 = sol.deleteDuplicates(l1)
    TmpUtil.printLinkedList(l1)
    TmpUtil.printLinkedList(l11)

    print()

    l1 = Solution.list2LinkedList([])
    l11 = sol.deleteDuplicates(l1)
    TmpUtil.printLinkedList(l1)
    TmpUtil.printLinkedList(l11)
