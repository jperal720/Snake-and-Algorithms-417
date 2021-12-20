class node:

    def __init__(self, data):
        block_obstacle = False  #is the node blocking the path?
        visited_node = False    #node has been visited previously
        global_goal = -1    #Total distance to goal
        local_goal = -1     #Distance to goal if we take an alternative route
        x = 0   #X position in the 2d space
        y = 0   #Y position in the 2d space
        self.neighbors = None   #Neighbors to current node
        self.parent = None  #Parent node of current node
