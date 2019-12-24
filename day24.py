from boilerplates import read_number_from_file, flatten_list

def print_state(s):
    for line in s:
        row = ""
        for i in line:
            row += {0: ".", 1: "#"}[i]
        print(row)

def get_adjecent(s, p):
    adj = []
    for add in [(-1, 0), (1, 0), (0, 1), (0, -1)]: # L, R, D, U
        if  -1 < (p[1] + add[1]) < 5 and -1 < (p[0] + add[0]) < 5:
            adj.append(s[p[1] + add[1]][p[0] + add[0]])
        else:
            adj.append(0)
    return adj

def advance(s):
    new_s = []
    for y in range(len(s)):
        r = []
        for x in range(len(s[0])):
            a = sum(get_adjecent(s, (x, y)))
            if s[y][x] == 0 and (a == 2 or a == 1):
                r.append(1)
            elif s[y][x] == 1 and a != 1:
                r.append(0)
            else:
                r.append(s[y][x])

        new_s.append(r)
    return new_s

def get_adjecent_recursion(s_s, p, level):
    if p == (2, 2):
        return []
    adj = []
    for add in [(-1, 0), (1, 0), (0, 1), (0, -1)]:  # L, R, D, U
        if (p[1] + add[1], p[0] + add[0]) == (2, 2):
            if add == (-1, 0):
                adj += [s_s[level + 1][i][4] for i in range(5)]
            if add == (1, 0):
                adj += [s_s[level + 1][i][0] for i in range(5)]
            if add == (0, 1):
                adj += [s_s[level + 1][0][i] for i in range(5)]
            if add == (0, -1):
                adj += [s_s[level + 1][4][i] for i in range(5)]
        elif p[1] + add[1] == 5:
            adj.append(s_s[level - 1][3][2])
        elif p[1] + add[1] == -1:
            adj.append(s_s[level - 1][1][2])
        elif p[0] + add[0] == 5:
            adj.append(s_s[level - 1][2][3])
        elif p[0] + add[0] == -1:
            adj.append(s_s[level - 1][2][1])
        else:
            adj.append(s_s[level][p[1] + add[1]][p[0] + add[0]])
    return adj

def advance_recursion(s_s, rng):
    new_s_s = []
    for lvl in range(rng[0], rng[1]):
        s = s_s[lvl]
        new_s = []
        for y in range(len(s)):
            r = []
            for x in range(len(s[0])):
                a = sum(get_adjecent_recursion(s_s, (x, y), lvl))
                if s[y][x] == 0 and (a == 2 or a == 1):
                    r.append(1)
                elif s[y][x] == 1 and a != 1:
                    r.append(0)
                else:
                    r.append(s[y][x])

            new_s.append(r)
        new_s_s.append(new_s)
    new_s_s.insert(0, s_s[0])
    new_s_s.append(s_s[-1])
    return  new_s_s

def get_bio(s):
    b = ""
    for y in range(len(s)):
        for x in range(len(s[0])):
            b = str(s[y][x]) + b

    return int(b, 2)

def part1(s):
    seen_states = set()
    seen_states.add(get_bio(s))
    while True:
        s = advance(s)
        bio = get_bio(s)
        if bio not in seen_states:
            seen_states.add(bio)
        else:
            #print_state(s)
            print("Part 1:", bio)
            break

def part2(s):
    empty_state = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    states = [empty_state[:], empty_state[:], s, empty_state[:], empty_state[:]]

    level_0 = 2

    rng = [1, 4]
    for a in range(200):
        states = advance_recursion(states, rng)

        if sum(flatten_list(states[1])) != 0:
            states.insert(0, empty_state[:])
            rng[1] += 1
            level_0 += 1
        if sum(flatten_list(states[-2])) != 0:
            states.append(empty_state[:])
            rng[1] += 1


    print("Part 2:", sum(flatten_list(states)))
    # for i, st in enumerate(states):
    #     print("=====", i - level_0)
    #     print_state(st)

state = read_number_from_file("day24", split="")
part1(state)
part2(state)