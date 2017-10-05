class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode (int(n % 10))
            if n > 9:
                node.next = tolist(n/10)
            return node
        return tolist(toint(l1) + toint(l2))

    # def addTwoNumbers(self, l1, l2):
    #     carry = 0
    #     root = n = ListNode(0)
    #     while l1 or l2 or carry:
    #         v1 = v2 = 0
    #         if l1:
    #             v1 = l1.val
    #             l1 = l1.next
    #         if l2:
    #             v2 = l2.val
    #             l2 = l2.next
    #         carry, val = divmod(v1 + v2 + carry, 10)
    #         n.next = ListNode(val)
    #         n = n.next
    #     return root.next



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
    line1 = [2,4,3]
    line2 = [5,6,4]
    l1 = stringToListNode(line1)
    l2 = stringToListNode(line2)
    ret = Solution().addTwoNumbers(l1, l2)
    #ret = Solution().equal(l2,2)
    out = listNodeToString(ret)
    print (out)

if __name__ == '__main__':
    main()


'''

'''