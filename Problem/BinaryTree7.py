""" Boundary order Traversal """


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def BoundaryTraversal(rootNode):
    BST_traversal = []
    CurrentLevel = []

    Queue = [rootNode, None]

    while len(Queue) > 0:
        if Queue[0] is not None:
            # CurrentNode value
            CurrentNode = Queue[0]

            # Remove Node
            Queue.pop(0)

            # Add Node value to CurrentLevel list
            CurrentLevel.append(CurrentNode)

            if CurrentNode.left is not None:
                Queue.append(CurrentNode.left)

            if CurrentNode.right is not None:
                Queue.append(CurrentNode.right)
        else:
            BST_traversal.append(CurrentLevel.copy())
            CurrentLevel.clear()

            if len(Queue) == 1:
                Queue.pop(0)
            else:
                Queue.pop(0)
                Queue.append(None)

    Boundary_traversal_value = []

    StartIndex = 1
    Boundary_traversal_value.append(BST_traversal[0][0].val)

    for i in range(1, len(BST_traversal)):
        if len(BST_traversal[i]) == 1:
            Boundary_traversal_value.insert(StartIndex, BST_traversal[i][0].val)
            StartIndex += 1
        else:
            # Insert First LeftView Element
            Boundary_traversal_value.insert(StartIndex, BST_traversal[i][0].val)
            StartIndex += 1

            # Insert First RightView Element
            Boundary_traversal_value.insert(StartIndex, BST_traversal[i][-1].val)

            TempIndex = StartIndex

            for j in range(1, len(BST_traversal[i]) - 1):
                LeafNode = BST_traversal[i][j]

                if LeafNode.left is None and LeafNode.right is None:
                    Boundary_traversal_value.insert(TempIndex, LeafNode.val)
    print(Boundary_traversal_value)


Root = Node(1)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(5)
Root.left.right.left = Node(8)
Root.left.right.right = Node(9)
Root.right.left = Node(6)
Root.right.right = Node(7)

BoundaryTraversal(Root)
