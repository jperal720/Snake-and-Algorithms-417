class Node:
    def __init__(self):
        #Neighboring Nodes
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        #Does it contain the head of the snake
        self.head = False
        #Does it contain a body node of the snake?
        self.body = False
        self.apple = False