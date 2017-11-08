# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        def isSym(L, R):
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        if root and root.left and root.right and root.left.val == root.right.val:
            return isSym(root.left,root.right)
        elif root and not(root.left or root.right):
            return True
        elif not root:
            return True
        else:
            return False


def stringToTreeNode(input):

    if not input:
        return None

    inputValues = [s for s in input]
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


def main():
    pline = []
    p = stringToTreeNode(pline)
    ret = Solution().isSymmetric(p)
    out = (ret)
    print(out)

if __name__ == '__main__':
    main()