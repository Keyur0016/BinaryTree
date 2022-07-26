""" Zigzag Conversion """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def ZigZagConversion(rootNode):
    """ zigzag conversion """

    LevelTraversal = []

    Queue = [rootNode, None]
    CurrentLevel = []

    while len(Queue) > 0:

        if Queue[0] is not None:
            CurrentNode = Queue[0]

            # Append CurrentNode value
            CurrentLevel.append(CurrentNode.val)

            Queue.pop(0)

            if CurrentNode.left is not None:
                Queue.append(CurrentNode.left)

            if CurrentNode.right is not None:
                Queue.append(CurrentNode.right)

        else:
            LevelTraversal.append(CurrentLevel.copy())
            CurrentLevel.clear()

            if len(Queue) == 1:
                Queue.pop(0)
            else:
                Queue.pop(0)
                Queue.append(None)

    ConvertZigzag = 0 
    for item in LevelTraversal:
        if ConvertZigzag == 0:
            print(item)
            ConvertZigzag = 1
        else:
            print(item[::-1])
            ConvertZigzag = 0


Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(60)

ZigZagConversion(Root)