# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l_1 = ListNode(1)
l_2 = l_1.next = ListNode(2)
l_3 = l_2.next = ListNode(3)

print(l_1.val)
print(l_1.next.val)
print(l_1.next.next.val)


def showListNode(LN):
    while LN:
        print(LN.val)
        LN = LN.next


def showListNodeBackward(LN):
    if LN is None:
        return
    showListNodeBackward(LN.next)
    print(LN.val)


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

showListNode(list1)
showListNodeBackward(list2)
