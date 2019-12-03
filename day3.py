from boilerplates import read_text_from_file
from timeit import timeit

wires = read_text_from_file(r"D:\AdventOfCode2019\probleminput\day3.txt", split=",")

def get_all_points(path):
    points = set()
    dist = dict()
    new_pos = (0, 0)

    steps = 0

    for instruction in path:
        direct = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}[instruction[0]]
        length = int(instruction[1:])

        next_steps = [(new_pos[0] + i * direct[0], new_pos[1] + i * direct[1]) for i in range(1, length + 1)]
        points.update(next_steps)
        dist.update([(next_steps[i], i + 1 + steps) for i in range(length)])

        new_pos = next_steps[-1]
        steps += length

    return points, dist

def solution2():
    points, dist_1 = get_all_points(wires[0])
    points_2, dist_2 = get_all_points(wires[1])

    crossings = points & points_2

    crossings_length = sorted([abs(cr[0]) + abs(cr[1]) for cr in crossings])[0]
    costs = sorted([dist_1[cr] + dist_2[cr] for cr in crossings])[0]


def solution2_print():
    points, dist_1 = get_all_points(wires[0])
    points_2, dist_2 = get_all_points(wires[1])

    crossings = points & points_2

    crossings_length = sorted([abs(cr[0]) + abs(cr[1]) for cr in crossings])
    costs = sorted([dist_1[cr] + dist_2[cr] for cr in crossings])

    print("Part 1:", crossings_length[0])
    print("Part 2:", costs[0])


solution2_print()

reps = 100
print(timeit(solution2, number=reps)/reps)
