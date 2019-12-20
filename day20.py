from boilerplates import read_text_from_file
from astar import astar_with_portals
from copy import deepcopy

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

def print_board(b, s, e, p = None):
    if p == None:
        p = []
    for y in range(len(b)):
        row = ""
        for x in range(len(b[y])):
            if (x, y) == s:
                row += "@"
            elif (x, y) == e:
                row += "="
            elif (x, y) in p:
                row += "O"
            else:
                row += b[y][x]
        print(row)

def try_portal_set(p_keys):
    c_board = board[:]
    for y in range(len(c_board)):
        for x in range(len(c_board[y])):
            if c_board[y][x] == "X":
                if portals[(x, y)] not in p_keys:
                    c_board[y] = c_board[y][:x] + "#" + c_board[y][x + 1:]
    c_portals = {}
    #print(p_keys)
    for p in portals:
        if portals[p] in p_keys:
            c_portals[p] = portals[p]
    #print(c_portals)
    return astar_with_portals(c_board, start_pos, end_pos, c_portals, walkable=".")

board = read_text_from_file("day20", nostrip=True)
orig_board = board[:]

portals = {}
portal_keys = []
start_pos = (0, 0)
end_pos = (0, 0)
for y in range(len(board)):
    for x in range(len(board[y])):
        if ord(board[y][x]) > 64:
            adjecents = get_adjecents(board, (x, y))
            portal = board[y][x]
            if "." in adjecents:
                if ord(adjecents[0]) > 64:
                    portal = adjecents[0] + portal
                    if portal != "AA" and portal != "ZZ":
                        board[y] = board[y][:x] + "X" + board[y][x + 1:]
                        board[y - 1] = board[y - 1][:x] + " " + board[y - 1][x + 1:]
                elif ord(adjecents[1]) > 64:
                    portal =  portal + adjecents[1]
                    if portal != "AA" and portal != "ZZ":
                        board[y] = board[y][:x] + "X " + board[y][x + 2:]
                elif ord(adjecents[2]) > 64:
                    portal = portal + adjecents[2]
                    if portal != "AA" and portal != "ZZ":
                        board[y] = board[y][:x] + "X" + board[y][x + 1:]
                        board[y + 1] = board[y + 1][:x] + " " + board[y + 1][x + 1:]
                else:
                    portal = adjecents[3] + portal
                    if portal != "AA" and portal != "ZZ":
                        board[y] = board[y][:x - 1] + " X" + board[y][x + 1:]


                if portal == "AA":
                    to_add = {0: (0, -1), 1: (1, 0), 2:(0, 1), 3:(-1, 0)}[adjecents.index(".")]
                    start_pos = (x + to_add[0], y + to_add[1])
                elif portal == "ZZ":
                    to_add = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[adjecents.index(".")]
                    end_pos = (x + to_add[0], y + to_add[1])
                else:
                    if portal not in portal_keys:
                        portal_keys.append(portal)
                    portals[(x, y)] = portal

print_board(orig_board, start_pos, end_pos)

min_length = len(try_portal_set(portal_keys)) - 1
print(min_length)


for portal in portal_keys:
    copy_keys = deepcopy(portal_keys)
    copy_keys.remove(portal)
    path = try_portal_set(copy_keys)
    #print_board(orig_board, start_pos, end_pos, path)
    if len(path) - 1 < min_length:
        min_length = len(path) - 1
    print("Removed", portal, "Length:", len(path) - 1)

print(min_length)



