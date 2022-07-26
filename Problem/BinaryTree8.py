""" Preorder Traversal and BST """

array = [2, 4, 3]


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


BSTRoot = None


def CreateBST(a1):
    """ Function which create BinarySearch Tree """

    if len(a1) == 0:
        return
    else:

        MidValue = len(a1) // 2

        Root = Node(a1[MidValue])

        Root.left = CreateBST(a1[:MidValue])
        Root.right = CreateBST(a1[MidValue+1:])

        return Root



