# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def showListNode(LN):
    while LN:
        print(LN.val)
        LN = LN.next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    flag_first = 1
    while l1 or l2:
        if l1 and not l2:
            if flag_first:
                listRet = l1
                list_head = listRet
                flag_first = 0
            else:
                listRet = l1
            return list_head
        elif l2 and not l1:
            if flag_first:
                listRet = l2
                list_head = listRet
                flag_first = 0
            else:
                listRet = l2
            return list_head
        else:
            if l1.val == l2.val:
                if flag_first:
                    listRet = l1
                    list_head = listRet
                    flag_first = 0
                else:
                    listRet = l1
                listRet = listRet.next
                listRet = l2
                listRet = listRet.next
                l1 = l1.next
                l2 = l2.next
            elif l1.val < l2.val:
                if flag_first:
                    listRet = l1
                    list_head = listRet
                    flag_first = 0
                else:
                    listRet = l1
                listRet = listRet.next
                l1 = l1.next
            elif l1.val > l2.val:
                if flag_first:
                    listRet = l2
                    list_head = listRet
                    flag_first = 0
                else:
                    listRet = l2
                listRet = listRet.next
                l2 = l2.next
    return list_head


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = mergeTwoLists(list1, list2)

list4 = list1   # 1
list_head = list4

list4 = list4.next
list4 = list2.next          # 3


showListNode(list4)
print("============")
showListNode(list_head)
