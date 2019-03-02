from TreeNode import TreeNode


def getMinimalBST(sortedSequence):
    if (0 == len(sortedSequence)):
        return None
    middleIndex = len(sortedSequence) // 2
    root = TreeNode(sortedSequence[middleIndex])
    root.left = getMinimalBST(sortedSequence[0:middleIndex])
    root.right = getMinimalBST(sortedSequence[middleIndex + 1:])
    return root
