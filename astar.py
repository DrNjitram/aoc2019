class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def get_other_pos(ports, p):
    portal_code = ports[p]
    for port in ports:
        if port != p and ports[port] == portal_code:
            return port
    raise ValueError

def get_adjecents(b, p):
    l = r = u = d= "#"
    try:
        u = b[p[1] - 1][p[0]]
    except:
        pass
    try:
        r = b[p[1]][p[0] + 1]
    except:
        pass
    try:
        d = b[p[1] + 1][p[0]]
    except:
        pass
    try:
        l = b[p[1]][p[0] - 1]
    except:
        pass
    return u, r, d, l

def astar(maze, start, end, diagonals = False, walkable = 0, dictdefault = 1):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)


    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #print(len(open_list), current_node.position)
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        if diagonals is True:
            adjecents = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            adjecents = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for new_position in adjecents: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if type(maze) == type(dict()):
                if maze.get(node_position, dictdefault) != walkable and node_position != end:
                    continue

            elif type(maze) == type(list()):
                # Make sure within range
                if node_position[1] > (len(maze) - 1) or node_position[1] < 0 or node_position[0] > (len(maze[len(maze) - 1]) - 1) or node_position[0] < 0:
                    continue

                # Make sure walkable terrain
                if maze[node_position[1]][node_position[0]] != walkable and node_position != end:
                    continue



            # Create new node
            new_node = Node(current_node, node_position)


            # Append
            #print("New kid", node_position)
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            #print("kid got added", child.position)
            # Add the child to the open list

            open_list.append(child)

def astar_with_portals(maze, start, end, portals, portal_marker = "X", diagonals = False, walkable = 0, dictdefault = 1):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #print(len(open_list), current_node.position)
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        if diagonals is True:
            adjecents = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            adjecents = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for new_position in adjecents: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if type(maze) == type(dict()):
                if maze.get(node_position, dictdefault) != walkable and node_position != end:
                    continue

            elif type(maze) == type(list()):

                # Make sure within range
                if node_position[1] > (len(maze) - 1) or node_position[1] < 0 or node_position[0] > (len(maze[node_position[1]]) - 1) or node_position[0] < 0:
                    #print(node_position, "OOB", (len(maze[len(maze) - 1]) - 1), (len(maze) - 1))
                    continue

                # Make sure walkable terrain
                if maze[node_position[1]][node_position[0]] != walkable and node_position != end:
                    if maze[node_position[1]][node_position[0]] == portal_marker and current_node != start_node:
                        node_position = get_other_pos(portals, node_position)
                        to_add = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[get_adjecents(maze, node_position).index(".")]
                        node_position = (node_position[0] + to_add[0], node_position[1] + to_add[1])
                        #print("Portalled", node_position)
                    else:
                        continue

                #print(node_position, "walkable")


            # Create new node
            new_node = Node(current_node, node_position)


            # Append
            #print("New kid", node_position)
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            #print("kid got added", child.position, child.f)
            # Add the child to the open list

            open_list.append(child)