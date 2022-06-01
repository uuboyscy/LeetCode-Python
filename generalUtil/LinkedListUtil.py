class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2LinkedList(inputList: list) -> ListNode:
    outputLinkedList = None
    tmpLinkedList = None
    if inputList == None or inputList.__len__() == 0:
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