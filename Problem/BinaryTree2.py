""" Vertical level order traversal """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


LevelDict = {}


def VerticalLevelTraversal(rootNode, level, dict):
    """ Vertical level vise traversal """

    if rootNode is None:
        return

    try:
        dict[level].append(rootNode.val)
    except:
        dict[level] = [rootNode.val]

    VerticalLevelTraversal(rootNode.left, level - 1, dict)
    VerticalLevelTraversal(rootNode.right, level + 1, dict)


def TopView():
    """ Print Topview of Binary tree"""
    global LevelDict

    print("Top view of BinaryTree")

    LevelList = list(LevelDict.keys())
    LevelList.sort()

    for item in LevelList:
        print(LevelDict[item][0])


def BottomView():
    """ Print Bottomview of BinaryTree """

    print("BottomView of BinaryTree ")

    LevelList = list(LevelDict.keys())
    LevelList.sort()

    for item in LevelList:
        print(LevelDict[item][-1])


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print Vertical level of BinaryTree

VerticalLevelTraversal(root, 0, LevelDict)

TopView()

BottomView()