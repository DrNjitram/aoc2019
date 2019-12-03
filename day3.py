from boilerplates import read_text_from_file
from time import time

wires = read_text_from_file(r"D:\AdventOfCode2019\probleminput\day3.txt", split=",")

grid = set()
distances_dict = dict()
crossings = set()

def fill_in_line(grid_set, start, direction, wire, other_wire, steps):
    direct = {"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}[direction[0]]
    length = int(direction[1:])

    while length > 0:
        steps += 1
        new_pos = (start[0] + direct[0], start[1] + direct[1])
        if new_pos + tuple([other_wire]) in grid_set:
            crossings.add(new_pos + tuple([wire, other_wire]))
        grid_set.add(new_pos + tuple([wire]))
        distances_dict[new_pos + tuple([wire])] = steps
        start = new_pos
        length -=1

    return start, steps

time_0 = time()
for wire_id, wire_insts in enumerate(wires):
    current_pos = (0, 0)
    current_steps = 0
    for inst in wire_insts:
        current_pos, current_steps = fill_in_line(grid, current_pos, inst, wire_id, 0 if wire_id == 1 else 1, current_steps)

distances = []
for cross in crossings:
    distances.append(distances_dict[(cross[0],cross[1], 0)] + distances_dict[(cross[0],cross[1], 1)])

print(sorted(distances)[0])
print(time() - time_0)
