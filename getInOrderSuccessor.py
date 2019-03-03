from TreeNode import *

def getInOrderSuccessor(TreeNode node):
    if node is None:
        return None
    if node.right is not None:
        return _getLeftmostChild(node.right)
    else:
        currentNode = node
        parent = node.parent
        while (parent is not None) and (parent.left != currentNode):
            currentNode = parent
            parent = parent.parent
        return parent

def _getLeftmostChild(TreeNode node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


