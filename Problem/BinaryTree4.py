""" Find Height of BinaryTree """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def Height(rootNode, height):
    if rootNode is None:
        return height - 1
    else:
        return max(Height(rootNode.left, height + 1),
                   Height(rootNode.right, height + 1))


Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(60)

print(Height(Root, 0))
