from boilerplates import read_text_from_file
from copy import deepcopy
from parse import parse, compile
import numpy as np
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def gdc(a, b):
    f_a = factors(a)
    f_b = factors(b)
    return sorted(f_a & f_b)[-1]

def div(n, d):
    return (n - d) / abs(n - d) if n-d else 0

def get_velocity(positions, velocties):
    changes = [np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0])]

    for i, a in enumerate(positions):
        for j in range(3):
            changes[i][j] = sum([div(comp_pos[j], a[j]) for comp_pos in positions])

    return changes[0] + velocties[0], changes[1] + velocties[1], changes[2] + velocties[2],  changes[3] + velocties[3]

def get_velocity_single(x_s, v_s):
    changes = np.array([0, 0, 0, 0])
    changes[0] = div(x_s[1], x_s[0]) + div(x_s[2], x_s[0]) + div(x_s[3], x_s[0])
    changes[1] = div(x_s[0], x_s[1]) + div(x_s[2], x_s[1]) + div(x_s[3], x_s[1])
    changes[2] = div(x_s[0], x_s[2]) + div(x_s[1], x_s[2]) + div(x_s[3], x_s[2])
    changes[3] = div(x_s[0], x_s[3]) + div(x_s[1], x_s[3]) + div(x_s[2], x_s[3])
    return changes + v_s

def update_positions(positions, velocities):
    return np.array([positions[0] + velocities[0], positions[1] + velocities[1], positions[2] + velocities[2],  positions[3] + velocities[3]])

def get_energy(positions, velocities):
    return sum(sum([abs(_) for _ in positions[i]])*sum(abs(_) for _ in velocities[i]) for i in range(len(positions)))

def part1(pos):
    vel = [np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0])]
    for i in range(0, 1000):
        vel = get_velocity(pos, vel)
        pos = update_positions(pos, vel)

    print("Part 1:", get_energy(pos, vel))

def flatten_list(n):
    nested_list = n[:]
    while nested_list:
        sublist = nested_list.pop(0)
        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist

def find_period(pos, axis):
    i = 0
    single_vel = np.array([0, 0, 0, 0])
    single_pos = np.array([pos[0][axis], pos[1][axis], pos[2][axis], pos[3][axis]])
    start_pos = deepcopy(single_pos)

    while True:
        single_vel = get_velocity_single(single_pos, single_vel)
        single_pos = single_pos + single_vel
        i += 1

        if np.array_equal(single_pos, start_pos) and np.array_equal(single_vel, np.array([0, 0, 0, 0])):

            return i

def lcm(n1, n2, n3):
    ans = (n1 * n2)//gdc(n1, n2)
    return (ans * n3)//gdc(ans, n3)

def part2(pos):
    a = find_period(deepcopy(pos), 0)
    b = find_period(deepcopy(pos), 1)
    c = find_period(deepcopy(pos), 2)
    answer = lcm(a, b, c)
    print("Part 2:", answer, a, b, c)

f = read_text_from_file("day12")

parser = compile("<x={}, y={}, z={}>")
pos_init = [np.array([int(i) for i in parser.parse(_)]) for _ in f]

part1(deepcopy(pos_init))
part2(deepcopy(pos_init))