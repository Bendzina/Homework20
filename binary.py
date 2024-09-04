class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def printLeafNodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=" ")

        self.printLeafNodes(node.left)
        self.printLeafNodes(node.right)

    def countEdges(self, node):
        if node is None:
            return 0

        left_edges = self.countEdges(node.left)
        right_edges = self.countEdges(node.right)

        return left_edges + right_edges + (1 if node.left or node.right else 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)    
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)


tree = BinaryTree(root)


print("Leaf Nodes:")
tree.printLeafNodes(tree.root)

print("\nNumber of cracks:")
print(tree.countEdges(tree.root))