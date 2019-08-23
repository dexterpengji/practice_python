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
