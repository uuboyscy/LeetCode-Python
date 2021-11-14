'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
the values in the list's nodes (i.e., only nodes themselves may be changed.)
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

    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None :
            return None
        nodeList = list()
        sortedNodeList = list()
        tmpHead = head
        while tmpHead != None:
            nodeList.append(tmpHead)
            tmpHead = tmpHead.next
        for n, i in enumerate(nodeList):
            if n % 2 == 0 and n < nodeList.__len__() - 1:
                sortedNodeList.append(nodeList[n + 1])
                sortedNodeList.append(i)
            elif n % 2 == 0 and n == nodeList.__len__() - 1:
                sortedNodeList.append(i)
            else:
                continue
        for n, i in enumerate(sortedNodeList):
            if n == sortedNodeList.__len__() - 1:
                i.next = None
            else:
                i.next = sortedNodeList[n + 1]

        return sortedNodeList[0]

class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        node = pre
        while pre.next != None and pre.next.next != None:
            l1 = pre.next
            l2 = pre.next.next
            nxt = l2.next
            l1.next = nxt
            l2.next = l1
            pre.next = l2
            pre = l1
        return node.next

if __name__ == '__main__':
    sol = Solution()
    s = [0, 1, 2, 3, 4]
    ll = sol.list2LinkedList(s)
    h1 = ll
    h2 = ll.next
    # TmpUtil.printLinkedList(ll)
    # TmpUtil.printLinkedList(h1)
    # TmpUtil.printLinkedList(h2)
    # print()
    # h2.next = h1
    # TmpUtil.printLinkedList(ll)
    # TmpUtil.printLinkedList(h1)
    # TmpUtil.printLinkedList(h2)
    # print(sol.swapPairs(ll))
    # for i in sol.swapPairs(ll):
    #     print(i.val)
    TmpUtil.printLinkedList(sol.swapPairs(ll))
    TmpUtil.printLinkedList(sol.swapPairs(sol.list2LinkedList([1])))
    TmpUtil.printLinkedList(sol.swapPairs(sol.list2LinkedList([1, 2])))
    TmpUtil.printLinkedList(sol.swapPairs(sol.list2LinkedList([1, 2, 3])))



