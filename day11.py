from boilerplates import read_number_from_file
from intcode import get_output

commands = read_number_from_file("day11", split=",")

direction = 0 # 0, up, 1, right, 2, bottom, 3, left
panels = {(0, 0): 1}
position = (0, 0)
pointer = 0
rel_offset = 0
halted = True
color = 0

while halted:
    if position in panels:
        color = panels[position]
    else:
        color = 0

    commands, pointer, output, output2, rel_offset, halted = get_output(commands, color, pointer, rel_offset)

    panels[position] = output[0]
    if output[1] == 1:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

    move = {0: (0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}
    position = position[0] + move[direction][0], position[1] + move[direction][1]


print(panels)
x_s = []
y_s = []
for panel in panels:
    x_s.append(panel[0])
    y_s.append(panel[1])

x_range = (min(x_s), max(x_s))
y_range = (min(y_s), max(y_s))

for y in range(y_range[1], y_range[0] - 1, -1):
    row = ""
    for x in range(x_range[0] , x_range[1] + 1):
        if (x, y) in panels:
            row += {0: " ", 1: "#"}[panels[(x, y)]]
        else:
            row += " "
    print(row)
