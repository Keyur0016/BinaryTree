""" BinaryTree Traversal methods """

""" Methods 
1. Preorder Traversal 
2. Postorder Traversal 
3. Inorder Traversal 
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def PreOrderTraversal(rootNode):
    if rootNode is None:
        print("None")
    else:
        print(rootNode.val)

        if rootNode.left is not None:
            PreOrderTraversal(rootNode.left)

        if rootNode.right is not None:
            PreOrderTraversal(rootNode.right)


def PostOrderTraversal(rootNode):
    if rootNode is None:
        print("None")
    else:
        if rootNode.left is not None:
            PostOrderTraversal(rootNode.left)
        if rootNode.right is not None:
            PostOrderTraversal(rootNode.right)
        print(rootNode.val)


def InOrderTraversal(rootNode):
    if rootNode is None:
        print("None")
    else:
        if rootNode.left is not None:
            InOrderTraversal(rootNode.left)
        print(rootNode.val)
        if rootNode.right is not None:
            InOrderTraversal(rootNode.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Preorder Traversal

PreOrderTraversal(root)

# Postorder Traversal

PostOrderTraversal(root)

# InOrder Traversal

InOrderTraversal(root)
