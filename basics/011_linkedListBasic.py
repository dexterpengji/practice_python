class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        curr = self.head
        counter = 0
        while curr:
            curr = curr.next
            counter += 1
        return counter

    def __str__(self):
        curr_node = self.head
        str_ret = ""
        while curr_node is not None:
            str_ret += "%s ==> " % curr_node.data
            curr_node = curr_node.next
        return str_ret

    def addToStart(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def addToEnd(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def addToNum(self, num, data):
        if data is None:
            return None
        node = Node(data)
        if len(self) < num:
            return -1
        curr_node = self.head
        if num == 0:
            node = Node(data, self.head)
            self.head = node
            return node
        if num < 0:
            return self.addToNum(len(self) + num + 1, data)
        for _ in range(num - 1):
            curr_node = curr_node.next
        node.next = curr_node.next
        curr_node.next = node
        return node

    def addAfterData(self, data, newData):
        if newData is None:
            return None
        node = Node(data)
        curr_node = self.head
        while curr_node is not None:
            if data == curr_node.data:
                node = Node(newData, curr_node.next)
                curr_node.next = node
                return node
            else:
                curr_node = curr_node.next
        return -1

    def addBeforeData(self, data, newData):
        if newData is None:
            return None
        node = Node(data)
        curr_node = self.head
        while curr_node is not None:
            if data == curr_node.next.data:
                node = Node(newData, curr_node.next)
                curr_node.next = node
                return node
            else:
                curr_node = curr_node.next
        return -1

    def find(self, data):       # first time data match
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def deleteData(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def deleteDataAlt(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def deleteNum(self, num):
        if num is None:
            return None
        if len(self) < num:
            return -1
        curr_node = self.head
        curr_node = self.head
        if num == 0:
            node = self.head.next
            self.head = node
            return node
        if num < 0:
            return self.deleteNum(len(self) + num)
        for _ in range(num - 1):
            curr_node = curr_node.next
        try:
            curr_node.next = curr_node.next.next
        except AttributeError:
            curr_node.next = None
        return


def showListNode(LN):
    while LN:
        print(LN.val)
        LN = LN.next


def showListNodeBackward(LN):
    if LN is None:
        return
    showListNodeBackward(LN.next)
    print(LN.val)


if __name__ == "__main__":
    A = Node(1)
    L_A = LinkedList(A)

    print(A)
    print(len(L_A))

    L_A.addToStart(0)
    print(L_A)

    L_A.addToEnd(2)
    print(L_A)

    L_A.addToNum(0, "addToNum_0")
    print(L_A)

    L_A.addToNum(3, "1_2")
    print(L_A)

    L_A.addToNum(-1, "add_-1")
    print(L_A)

    L_A.addToNum(-3, "add_-3")
    print(L_A)

    L_A.addAfterData(0, "after_0")
    print(L_A)

    L_A.addBeforeData(0, "before_0")
    print(L_A)

    print(L_A.find(0))
    print(L_A.find("does not exist"))

    L_A.deleteData(0)
    print(L_A)

    L_A.deleteData("before_0")
    print(L_A)

    L_A.deleteDataAlt("after_0")
    print(L_A)

    L_A.deleteNum(0)
    print(L_A)

    L_A.deleteNum(2)
    print(L_A)

    L_A.deleteNum(-2)
    print(L_A)

    L_A.deleteNum(-4)
    print(L_A)
