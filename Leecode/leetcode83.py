class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            print(cur.val)
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next

        return head

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
    line1 = [2,3,4,4,4]
    l1 = stringToListNode(line1)
    ret = Solution().deleteDuplicates(l1)
    out = listNodeToString(ret)
    print (out)

if __name__ == '__main__':
    main()