class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def length(self,l):
        slist = l
        count = 0
        while slist:
            slist = slist.next
            count += 1
        return count

    def equal(self,l,len):
        new = guard_node = ListNode(0)
        for _ in range(len):
            new.next = ListNode(0)
            new = new.next
        link = guard = l
        for i in range(Solution().length(l)-1):
            link = link.next
        link.next = guard_node.next
        return guard

    def addTwoNumbers(self, l1, l2):
        carry = 0
        node = guard_node = ListNode(0)
        if Solution().length(l1) < Solution().length(l2):
            len = abs(Solution().length(l2) - Solution().length(l1))
            l1 = Solution().equal(l1,len)
        elif Solution().length(l1) > Solution().length(l2):
            len = abs(Solution().length(l2) - Solution().length(l1))
            l2 = Solution().equal(l2, len)
        while l1 and l2:
            if l1.val+l2.val+carry < 10:
                node.next = ListNode(l1.val+l2.val+carry)
                carry = 0
            else:
                node.next = ListNode(l1.val+l2.val-10+carry)
                carry = 1
            l1 = l1.next
            l2 = l2.next
            node = node.next
        if carry != 0:
            node.next = ListNode(carry)
            node = node.next

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
    line1 = [1,8]
    line2 = [0]
    l1 = stringToListNode(line1)
    l2 = stringToListNode(line2)
    ret = Solution().addTwoNumbers(l1, l2)
    #ret = Solution().equal(l2,2)
    out = listNodeToString(ret)
    print (out)

if __name__ == '__main__':
    main()


'''
def addTwoNumbers(self, l1, l2):
       def toint(node):
           return node.val + 10 * toint(node.next) if node else 0
       def tolist(n):
           node = ListNode (n % 10)
           if n > 9:
               node.next = tolist(n/10)
           return node
       return tolist(toint(l1) + toint(l2))
'''