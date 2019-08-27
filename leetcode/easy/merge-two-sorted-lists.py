# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def showListNode(LN):
    while LN:
        print(LN.val)
        LN = LN.next


def showListNodeBackward(LN):
    if LN is None:
        return
    showListNodeBackward(LN.next)
    print(LN.val)


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    return list_head


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

ln = ListNode(None)


def makeListNode(x, ln):
    if x < 10:
        x += 1
        ln.next = ListNode(x)
        makeListNode(x, ln)


showListNodeBackward(list1)
