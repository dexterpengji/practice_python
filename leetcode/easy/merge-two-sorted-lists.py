import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.data)


def showListNode(head):
    while head:
        print("%s ==> " % head.val, end="")
        head = head.next
    print("")


# time complexity: O(n) | 36ms
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # if none
    if l1 is None and l2 is None:
        return None
    elif l1 is None and l2 is not None:
        return l2
    elif l1 is not None and l2 is None:
        return l1
    else:  # if no list is none
        if l1.val <= l2.val:  # choose the head value
            head_ret = ListNode(l1.val)
            l1 = l1.next
        else:
            head_ret = ListNode(l2.val)
            l2 = l2.next
        curr_node = head_ret
        while l1 and l2:  # choose the value of the next node
            if curr_node.next is not None:  # move to the end, if can be changed to while, but it will be slower
                curr_node = curr_node.next
            if l1.val <= l2.val:  # choose the value as l1
                curr_node.next = ListNode(l1.val)
                l1 = l1.next
            else:  # choose the value as l2
                curr_node.next = ListNode(l2.val)
                l2 = l2.next
        if l1 and not l2:  # if l2 has no more node
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = l1
        elif l2 and not l1:  # if l2 has no more node
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = l2
        return head_ret


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

showListNode(head1)
showListNode(head2)
timeStart = time.time()
head3 = mergeTwoLists(head1, head2)
print("Time spent: %f" % (time.time() - timeStart))
showListNode(head3)
