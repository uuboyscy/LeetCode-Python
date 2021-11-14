'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
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
    @staticmethod
    def list2LinkedList(inputList: list) -> ListNode:
        outputLinkedList = None
        tmpLinkedList = None
        for n, i in enumerate(inputList[::-1]):
            outputLinkedList = ListNode(i)
            outputLinkedList.next = tmpLinkedList
            tmpLinkedList = outputLinkedList

        return outputLinkedList

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedList = []
        while l1 != None or l2 != None:

            if l1 == None:
                while l2 != None:
                    # print(1, l2.val)
                    mergedList.append(l2.val)
                    l2 = l2.next
                return self.list2LinkedList(mergedList)
            elif l2 == None:
                while l1 != None:
                    # print(2, l1.val)
                    mergedList.append(l1.val)
                    l1 = l1.next
                return self.list2LinkedList(mergedList)

            if l1.val >= l2.val:
                # print(3, l2.val)
                mergedList.append(l2.val)
                l2 = l2.next
            else:
                # print(4, l1.val)
                mergedList.append(l1.val)
                l1 = l1.next

        return self.list2LinkedList(mergedList)

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

if __name__ == '__main__':
    sol = Solution()
    intersecList = [1, 8, 4, 5]
    l1 = Solution.list2LinkedList([0])
    l2 = Solution.list2LinkedList([5, 6])

    print(sol.mergeTwoLists(l1, l2).val)
    print(sol.mergeTwoLists(l1, l2).next.val)
    print([1].__len__())
    print(Solution.list2LinkedList([1]))
    # print(sol.mergeTwoLists(l1, l2).next.next.val)
    # print(sol.mergeTwoLists(l1, l2).next.next.next.val)



