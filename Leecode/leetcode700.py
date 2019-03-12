
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):
    if not input:
        return None

    root = TreeNode(int(input[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input):
        node = nodeQueue[front]
        front = front + 1

        item = input[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(input):
            break

        item = input[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current <= len(queue)-queue.count(None):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"



def searchBST(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    # if root and val < root.val: return self.searchBST(root.left, val)
    # elif root and val > root.val: return self.searchBST(root.right, val)
    # return root

    while root:
        if root.val == val:
            return root
        elif val > root.val:
            root = root.right
        else:
            root = root.left


a = stringToTreeNode([4,2,7,1,"null",5])
print(a.right.val)
print(treeNodeToString(a))
print(searchBST(a,2).left.val)
