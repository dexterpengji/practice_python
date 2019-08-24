"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def showAllNodes(self):
        node_obj = self
        chainMark = ""
        while node_obj is not None:
            print(chainMark + "%d" % node_obj.val, end="")
            node_obj = node_obj.next
            chainMark = " -> "
        print("")


# time complexity: O(n)
def addTwoNumbers(l1: ListNode, l2: ListNode, highDigit=0) -> ListNode:
    if l1 is not None or l2 is not None or highDigit != 0:
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)
        sum_pre = (l1.val + l2.val + highDigit)
        sum_nod, highDigit = sum_pre % 10, sum_pre // 10
        ret = ListNode(int(sum_nod))
        ret.next = addTwoNumbers(l1.next, l2.next, highDigit)
        return ret


L1 = ListNode(2)
L1.next = ListNode(4)
L1.next.next = ListNode(3)

L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next = ListNode(4)

L1.showAllNodes()
L2.showAllNodes()

L3 = addTwoNumbers(L1, L2)
L3.showAllNodes()
