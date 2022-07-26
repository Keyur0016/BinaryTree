""" Level order Traversal """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def LevelOrderTraversal(rootNode):
    """ Horizontal level order Traversal """

    print("LevelOrder Traversal")

    Queue = [rootNode]

    while len(Queue) > 0:
        CurrentNode = Queue[0]

        # Print CurrentNode value
        print(CurrentNode.val)

        # Remove CurrentNode from Queue
        Queue.pop(0)

        if CurrentNode.left is not None:
            Queue.append(CurrentNode.left)

        if CurrentNode.right is not None:
            Queue.append(CurrentNode.right)


def LevelByLevelPrint(rootNode):
    print("Level By Level printing")

    Queue = [rootNode, None]

    global Output
    Output = []
    CurrentLevel = []

    while len(Queue) > 0:

        if Queue[0] is not None:
            CurrentNode = Queue[0]

            # Add CurrentNode value to List
            CurrentLevel.append(CurrentNode.val)

            # Remove this Node From Queue
            Queue.pop(0)

            if CurrentNode.left is not None:
                Queue.append(CurrentNode.left)

            if CurrentNode.right is not None:
                Queue.append(CurrentNode.right)

        else:
            Level = CurrentLevel.copy()
            Output.append(Level)
            CurrentLevel.clear()

            if len(Queue) == 1:
                Queue.pop(0)
            else:
                Queue.pop(0)
                Queue.append(None)

    print(Output)


def LeftView():
    global Output

    print("LeftView")

    for item in Output:
        print(item[0])


def RightView():
    """ RightView of BinaryTree """

    global Output

    print("RightView")

    for item in Output:
        print(item[-1])


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print LevelByLevel Traversal

LevelOrderTraversal(root)

LevelByLevelPrint(root)

LeftView()

RightView()
