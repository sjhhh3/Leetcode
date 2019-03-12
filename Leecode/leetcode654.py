def constructMaximumBinaryTree(nums):
    dummy = root = TreeNode(0)

    def makemaxbst(node, left, right):
        if right > left:
            maxpos = nums.index(max(nums[left:right]))
            node = TreeNode(nums[maxpos])
            print(node.val)
            makemaxbst(node.left, left, maxpos)
            makemaxbst(node.right, maxpos + 1, right)

    makemaxbst(root, 0, len(nums))
    return dummy


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

print(constructMaximumBinaryTree([3,2,1,6,0,5]))