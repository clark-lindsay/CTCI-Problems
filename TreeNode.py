class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.getInorderTraversal()

    def getInorderTraversal(self):
        if self is not None:
            traversal = list()
            self._inOrderTraversal(traversal)
            return str(traversal)
        return ''

    def _inOrderTraversal(self, sequence):
        if self is None:
            sequence.append(None)
        else:
            if self.left is not None:
                self.left._inOrderTraversal(sequence)
            sequence.append(self.value)
            if self.right is not None:
                self.right._inOrderTraversal(sequence)