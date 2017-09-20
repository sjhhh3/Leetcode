class ListNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.root = ListNode()

    def append(self,data):
        new_node = ListNode(data)
        cur = self.root
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        elems = []
        cur_node = self.root
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)



def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return None

    node = guard_node = ListNode(0)

    while l1 and l2:
        if l1.data <= l2.data:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    if l1 or l2:
        node.next = l1 or l2

    return guard_node.next


l1 = LinkedList()
l1.append(34)
l1.append(46)
l1.append(78)
l1.display()

l2 = LinkedList()
l2.append(14)
l2.append(26)
l2.append(38)
l2.display()

mergeTwoLists(l1,l2)