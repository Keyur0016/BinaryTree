""" Check Tree is Balanced or not """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def LeftHeight(rootNode, height):
    """ Function is check BinaryTree is Balanced or not """

    if rootNode is None:
        return height - 1
    else:
        return LeftHeight(rootNode.left, height + 1)


def RightHeight(rootNode, height):
    if rootNode is None:
        return height - 1
    else:
        return RightHeight(rootNode.right, height + 1)


def Traversal(rootNode):
    if rootNode is None:
        return None
    else:
        Traversal(rootNode.left)

        # Calculate Left and Right subtree height from this Node
        LeftTreeHeight = LeftHeight(rootNode, 0)
        RightTreeHeight = RightHeight(rootNode, 0)

        if LeftTreeHeight - RightTreeHeight <= 1:
            CheckStatus = 1
        else:
            return False

        Traversal(rootNode.right)

    if CheckStatus == 1:
        return True


Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(60)

LeftHeightValue = LeftHeight(Root, 0)
RightHeightValue = RightHeight(Root, 0)
Traversal(rootNode=Root)
