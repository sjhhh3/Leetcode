class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):

    if not input:
        return None

    inputValues = input
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


myinput = stringToTreeNode([5,3,6,2,4,'null',8,1,'null','null','null',7,9])

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        li = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()
                li.append(node)
                root = node.left

        r = dummy = li.pop()
        while li:
            r.right = li.pop()
            r = r.right
            r.left = None
        return dummy


a = Solution()
print(a.increasingBST(myinput).right.right.right.right.right.right.right.val)
