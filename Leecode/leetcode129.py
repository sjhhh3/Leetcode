def sumNumbers(root):
    # DFS
    def findpath(root, tmppath):
        tmppath += str(root.val)
        if not root.left and not root.right:
            allpath.append(tmppath)
        else:
            findpath(root.left, tmppath)
            findpath(root.right, tmppath)

    allpath = []
    findpath(root, "")
    return allpath


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node3

print(sumNumbers(node1))