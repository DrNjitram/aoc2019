from boilerplates import read_number_from_file
from intcode import get_output
from astar import astar

def print_plane(brd, bot_pos, trg, oxygen):
    x_s = []
    y_s = []

    for panel in brd:
        x_s.append(panel[0])
        y_s.append(panel[1])

    for y in range(min(y_s), max(y_s) + 1):
        row = ""
        for x in range(min(x_s), max(x_s) + 1):
            if (x, y) == bot_pos:
                row += "X"
            elif (x, y) == trg:
                row += "="
            elif (x, y) == (0, 0):
                row += "D"
            elif (x, y) == oxygen:
                row += "O"
            else:
                row += {0: "#", 1: ".", -1: " ", 2: "O"}[brd.get((x, y), -1)]

        print(row)

def get_input(known, p, unk, last_p, target, dead, debug = False):
    inp = -1
    if target == None:
        distances = {}
        for u in unk:
            distances[abs(u[0] - p[0]) + abs(u[1] - p[1])] = u

        target = distances[min(distances.keys())]

    delta = target[0] - p[0], target[1] - p[1]
    if debug:
       print("Target data:", p, target, delta)
    if delta[0] == 0 or delta[1] == 0:
        if delta[0] < 0:  # move E
            if known.get((p[0] - 1, p[1]), 1) != 0:
                inp = 3
        elif delta[0] > 0:  # move W
            if known.get((p[0] + 1, p[1]), 1) != 0:
                inp = 4
        elif delta[1] < 0:  # move N
            if known.get((p[0], p[1] - 1), 1) != 0:
                inp = 1
        else:
            if known.get((p[0], p[1] + 1), 1) != 0:
                inp = 2

        if abs(delta[0]) + abs(delta[1]) == 1:
            target = None

        if inp != -1:
            if {1: 2, 2: 1, 3: 4, 4: 3}[inp] == last_p:
                inp = -1

    if inp == -1 or not (delta[0] == 0 or delta[1] == 0):
        potentials = []
        if delta[0] < 0:  # move W
            if known.get((p[0] - 1, p[1]), 1) != 0:
                potentials.append(3)
        if delta[0] > 0:  # move E
            if known.get((p[0] + 1, p[1]), 1) != 0:
                potentials.append(4)
        if delta[1] < 0:  # move N
            if known.get((p[0], p[1] - 1), 1) != 0:
                potentials.append(1)
        if delta[1] > 0: # move S
            if known.get((p[0], p[1] + 1), 1) != 0:
                potentials.append(2)

        print(potentials)

        #Remove if in dead
        for potent in potentials:
            if (p[0] + mov_dict[potent][0], p[1] + mov_dict[potent][1]) in dead:
                potentials.remove(potent)

        print(potentials)

        if len(potentials) > 1:
            for potent in potentials:
                if {1: 2, 2: 1, 3: 4, 4: 3}[potent] == last_p:
                    potentials.remove(potent)

        if len(potentials) == 0: #should have hit a dead end, so backtrack
            dead.append(p)
            potentials = [c for c in range(1, 5) if known.get((p[0] + mov_dict[c][0], p[1] + mov_dict[c][1]), 1) != 0]

        print(potentials)

        if len(potentials) > 1:
            for potent in potentials:
                if {1: 2, 2: 1, 3: 4, 4: 3}[potent] == last_p:
                    potentials.remove(potent)

        if len(potentials) > 1:
            # Remove if in dead
            for potent in potentials:
                if (p[0] + mov_dict[potent][0], p[1] + mov_dict[potent][1]) in dead:
                    potentials.remove(potent)

        print(potentials)



        print(potentials)
        inp = potentials[0]

    return inp, target, dead

def execute_inputs(cmd, known, current = (0, 0), pointer = 0, rel_off = 0, debug = False):
    unknown = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    dead_nodes = []
    l_p = -1

    hlt = True
    target = None
    oxy = None

    i = 0

    while  hlt:
        direction, target, dead_nodes = get_input(known, current, unknown, l_p, target, dead_nodes, debug)

        for a in [1, 2, 3, 4]:
            if a != direction:
                other = get_output(cmd[:], a, pointer, rel_off)
                movement_vector = mov_dict[a]  # N, S, W, E
                next_pos = (current[0] + movement_vector[0], current[1] + movement_vector[1])
                if next_pos not in known:
                    known[next_pos] = other[2][0]

                if other[2][0] == 1:
                    for b in [1, 2, 3, 4]:
                        movement_vector = mov_dict[b]  # N, S, W, E
                        next_next_pos = (next_pos[0] + movement_vector[0], next_pos[1] + movement_vector[1])
                        if next_next_pos not in unknown and next_next_pos not in known:
                            unknown.append(next_next_pos)

                if next_pos in unknown:
                    unknown.remove(next_pos)




        cmd, pointer, out, zero_out, rel_off, hlt = get_output(cmd, direction, pointer, rel_off)


        movement_vector = mov_dict[direction]  # N, S, W, E
        next_pos = (current[0] + movement_vector[0], current[1] + movement_vector[1])
        known[next_pos] = out[0]
        l_p = direction

        if debug:
            print("Output Data:", direction, next_pos, out[0])

        if next_pos in unknown:
            unknown.remove(next_pos)

        if out[0] == 1:  # Actually move
            current = next_pos
        elif out[0] == 2: # Found it
            known[next_pos] = 1
            current = next_pos
            oxy = current


        for add in (0, -1), (0, 1), (1, 0), (-1, 0):
            t = (current[0] + add[0], current[1] + add[1])
            if t not in known and t not in unknown:
                unknown.append(t)

        i += 1

        if debug:
            print("Misc:", target, direction, unknown)
            print_plane(known, current, target, oxy, unknown)
            print("============================", i)
        else:
            print(i)

        if i > 2000 or len(unknown) == 0:
            break

    return known, current, oxy

def get_closest(cur, unk):
    distances = [abs(cur[0] - u[0]) +abs(cur[1] - u[1]) for u in unk]
    return unk[distances.index(min(distances))]

def mov(cmd, known, current = (0, 0), pointer = 0, rel_off = 0, debug = False):
    unknown = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    hlt = True
    oxy = None

    i = 0
    while hlt and len(unknown) > 0:


        #print_plane(known_pos, current, unknown[0], oxy)
        #print(current, unknown[0], abs(current[0] - unknown[0][0]) + abs(current[1] - unknown[0][1]))


        path = astar(known, current, unknown[0], walkable=1, dictdefault=0, diagonals=False)

        for p in range(1, len(path)):

            direction = rev_mov_dict[(path[p][0] - current[0], path[p][1] - current[1])]

            for a in [1, 2, 3, 4]:
                if a != direction:
                    other = get_output(cmd[:], a, pointer, rel_off)
                    movement_vector = mov_dict[a]  # N, S, W, E
                    next_pos = (current[0] + movement_vector[0], current[1] + movement_vector[1])
                    if next_pos not in known:
                        known[next_pos] = other[2][0]
                    if other[2][0] == 0 and next_pos in unknown:
                        unknown.remove(next_pos)


            cmd, pointer, out, zero_out, rel_off, hlt = get_output(cmd, direction, pointer, rel_off)
            #print(current, path[p], direction, out)


            movement_vector = mov_dict[direction]  # N, S, W, E
            next_pos = (current[0] + movement_vector[0], current[1] + movement_vector[1])
            known[next_pos] = out[0]

            print_plane(known_pos, current, unknown[0], oxy)

            if next_pos in unknown:
                unknown.remove(next_pos)

            i += 1
            print("\r", round((i/1877)*100, 2), end="")

            if out[0] == 1:  # Actually move
                current = next_pos

                for add in (0, -1), (0, 1), (1, 0), (-1, 0):
                    t = (current[0] + add[0], current[1] + add[1])
                    if t not in known and t not in unknown:
                        unknown.insert(0, t)



            elif out[0] == 2: # Found it
                known[next_pos] = 1
                current = next_pos
                oxy = current
            else: # hit a wall and regenerate position
                break


        # if i > 2500:
        #     break

    return oxy



mov_dict = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
rev_mov_dict = {(0, -1):1, (0, 1):2, (-1, 0):3, (1, 0):4}
commands = read_number_from_file("day15", split=",")

known_pos = {(0, 0): 1} #1 walkable, 0 wall


oxy = mov(commands[:], known_pos, debug=True)

print_plane(known_pos, None, None, oxy)
print(len(astar(known_pos, (0, 0), oxy)))

max_len = 0

for p in known_pos:
    if known_pos[p] == 1:
        length = len(astar(known_pos, p, oxy)) - 1
        if length > max_len:
            max_len = length

print(max_len)


