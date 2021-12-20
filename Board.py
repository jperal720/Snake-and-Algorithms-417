from Node import Node

class Board():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.board = [None] * self.x

        for rows in range(self.x):
            r = [None] * self.y
            for columns in range(self.y):
                node = Node()

                if(columns == 0 ):
                    #make it so no left neighbor
                    node.left = None
                else:
                    #left neighbor
                    node.left = r[columns - 1]
                if(columns == self.y - 1):
                    #make it so no right neighbor
                    node.right = None
                else:
                    #right neighbor'
                    node.right = r[columns + 1]
                if (rows == 0):
                    #make it so no upper neighbor
                    node.up = None
                else:
                    #upper neighbor
                    node.up = r[rows - 1]
                if (rows == self.x - 1):
                    #make it so no down neighbor
                    node.down = None
                else:
                    #down neighbor
                    node.down = r[rows + 1]
                node.colour = 'black'
                node.head = False
                node.body = False
                r[columns] = node

            self.board[rows] = r