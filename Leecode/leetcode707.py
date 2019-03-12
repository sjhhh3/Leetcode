class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size or index < 0:
            return -1
        else:
            curnode = self.head
            for _ in range(index):
                curnode = curnode.next
            return curnode.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        newnode = Node(val)
        cur = self.head
        if not cur:
            self.head = newnode
        else:
            while cur and cur.next:
                cur = cur.next
            cur.next = newnode
        self.size += 1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)

        newnode = Node(val)
        curnode = self.head
        for _ in range(index-1):
            curnode = curnode.next
        newnode.next = curnode.next
        curnode.next = newnode
        self.size += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        curnode = self.head
        for _ in range(index-1):
            curnode = curnode.next
        curnode.next = curnode.next.next
        self.size -= 1

obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(3)
obj.addAtTail(4)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

print(obj.get(1))
obj.addAtIndex(1, 7)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))