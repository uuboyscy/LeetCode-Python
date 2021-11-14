'''
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        head1Amount = 0
        head2Amount = 0
        m = 0
        longList = None
        shortList = None
        outputList = None

        while head1 != None:
            head1 = head1.next
            head1Amount += 1
        while head2 != None:
            head2 = head2.next
            head2Amount += 1

        if head1Amount > head2Amount:
            longList = l1
            shortList = l2
            m = head1Amount - head2Amount
        else:
            longList = l2
            shortList = l1
            m = head2Amount - head1Amount

        for i in range(0, m):
            addedZeroNode = ListNode(0, shortList)
            shortList = addedZeroNode

        addedFirstZeroNode = ListNode(0, longList)
        longList = addedFirstZeroNode
        addedFirstZeroNode = ListNode(0, shortList)
        shortList = addedFirstZeroNode

        # TmpUtil.printLinkedList(longList)
        # TmpUtil.printLinkedList(shortList)

        outputList = longList
        ## Sum of the first nodes of two list
        while longList != None:
            longList.val += shortList.val
            longList = longList.next
            shortList = shortList.next
        longList = outputList
        while longList != None:
            longList.val -= 0 if longList.val < 10 else 10
            if longList.next != None:
                longList.val += 0 if longList.next.val < 10 else 1
            longList = longList.next

        return outputList if outputList.val != 0 else outputList.next

class Solution2:
    @staticmethod
    def list2LinkedList(inputList: list) -> ListNode:
        outputLinkedList = None
        tmpLinkedList = None
        for n, i in enumerate(inputList[::-1]):
            outputLinkedList = ListNode(i)
            outputLinkedList.next = tmpLinkedList
            tmpLinkedList = outputLinkedList

        return outputLinkedList

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        nodeList1 = list()
        nodeList2 = list()
        outputList = None
        sumOfTwoNodes = 0
        idx = 0

        while head1 != None:
            nodeList1.append(head1)
            head1 = head1.next
        while head2 != None:
            nodeList2.append(head2)
            head2 = head2.next

        while True:
            tmpNodeVal1 = 0 if (nodeList1.__len__() - 1 - idx < 0) else nodeList1[nodeList1.__len__() - 1 - idx].val
            tmpNodeVal2 = 0 if (nodeList2.__len__() - 1 - idx < 0) else nodeList2[nodeList2.__len__() - 1 - idx].val
            sumOfTwoNodes = tmpNodeVal1 + tmpNodeVal2 + int(sumOfTwoNodes/10)
            outputList = ListNode(sumOfTwoNodes % 10, outputList)
            idx += 1

            if (nodeList1.__len__() - 1 - idx < 0) and (nodeList2.__len__() - 1 - idx < 0):
                if int(sumOfTwoNodes/10) > 0:
                    outputList = ListNode(1, outputList)
                break

        return outputList


if __name__ == '__main__':
    sol = Solution2()

    l1 = [9]
    l2 = [3, 2, 3, 4]
    ll1 = sol.list2LinkedList(l1)
    ll2 = sol.list2LinkedList(l2)
    TmpUtil.printLinkedList(sol.addTwoNumbers(ll1, ll2))

    l1 = [9]
    l2 = [3, 9, 9, 4]
    ll1 = sol.list2LinkedList(l1)
    ll2 = sol.list2LinkedList(l2)
    TmpUtil.printLinkedList(sol.addTwoNumbers(ll1, ll2))

    l1 = [9]
    l2 = [5]
    ll1 = sol.list2LinkedList(l1)
    ll2 = sol.list2LinkedList(l2)
    TmpUtil.printLinkedList(sol.addTwoNumbers(ll1, ll2))
