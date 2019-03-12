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


myinput = stringToTreeNode([3,9,20,15,7])

#
# def increasingBST(root):
#     global newroot
#     newroot = TreeNode(-1)
#     tem = newroot
#
#     def rectra(root):
#         global newroot
#         if root:
#             rectra(root.left)
#             newroot.left = None
#             newroot.right = root
#             newroot = root
#             rectra(root.right)
#
#     rectra(root)
#     return tem
#
# print(increasingBST(myinput).right.val)

def averageOfLevels(root):

    info = []

    def dfs(node, depth=0):
        if node:
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

    dfs(root)

    return [s / float(c) for s, c in info]

print(averageOfLevels(myinput))