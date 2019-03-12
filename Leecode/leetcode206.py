class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseList(head):
    # if not head or not head.next:
    #     return head
    #
    # p = reverseList(head.next)
    # head.next.next = head
    # head.next = None
    # return p
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.next = b
b.next = c
c.next = d

print(reverseList(a))