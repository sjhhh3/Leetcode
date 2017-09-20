class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        node = guard_node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 or l2:
            node.next = l1 or l2
        return guard_node.next

# def stringToIntegerList(input):
#     input = input.strip()
#     input = input[1:-1]
#     return [int(number) for number in input.split(",")]

def stringToListNode(input):
    # Generate list from the input
    numbers = input
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return result[:-2]

def main():
    line1 = [23,44]
    line2 = [2,6]
    l1 = stringToListNode(line1)
    l2 = stringToListNode(line2)
    ret = Solution().mergeTwoLists(l1, l2)

    out = listNodeToString(ret)
    print (out)

if __name__ == '__main__':
    main()