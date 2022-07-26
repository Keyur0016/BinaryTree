""" Check for Mirror BinaryTree """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


TreeTraversal = []


def InorderTraversal(rootNode):
    """ BinaryTree Inorder Traversal method """

    global TreeTraversal

    if rootNode is None:
        print(None)
    else:
        if rootNode.left is not None:
            InorderTraversal(rootNode.left)
        TreeTraversal.append(rootNode.val)
        if rootNode.right is not None:
            InorderTraversal(rootNode.right)


MirrorTraversal = []


def MirrorTreeInorderTraversal(rootNode):
    """ Mirror tree Inorder Traversal """

    global MirrorTraversal

    if rootNode is None:
        print("None")
    else:
        if rootNode.right is not None:
            MirrorTreeInorderTraversal(rootNode.right)
        MirrorTraversal.append(rootNode.val)
        if rootNode.left is not None:
            MirrorTreeInorderTraversal(rootNode.left)


def CheckMirrorTree():
    global MirrorTraversal
    global TreeTraversal

    if TreeTraversal == MirrorTraversal[::-1]:
        print("Yes Tree is Mirror")
    else:
        print("No Tree is not Mirror")


Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(60)

InorderTraversal(Root)
MirrorTreeInorderTraversal(Root)
CheckMirrorTree()
