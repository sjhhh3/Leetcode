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


root = stringToTreeNode([1,3,2,4,5,6])

global maxlen
maxlen = 1

def trav(root):
    global maxlen
    if not root: return 0
    if not root.left and not root.right: return 1
    for child in (root.left, root.right):
        depth = trav(child) + 1
        maxlen = max(depth, maxlen)
    return maxlen


trav(root)
print(maxlen)