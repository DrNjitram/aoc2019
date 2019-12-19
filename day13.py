from boilerplates import read_number_from_file
from intcode import get_output

def chunks(L, n):
    for i in range(0, len(L), n):
        yield L[i:i+n]

def print_board(tls, printing = True):
    brd = {}
    for t in tls:
        brd[(t[0], t[1])] = t[2]

    if printing:
        x_s = []
        y_s = []

        for panel in brd:
            x_s.append(panel[0])
            y_s.append(panel[1])

        for y in range(0, max(y_s) + 1):
            row = ""
            for x in range(0, max(x_s) + 1):
                row += {0: " ", 1: "#", 2: "#", 3: "-", 4: "*"}[brd.get((x, y), 0)]
            print(row)
        print(brd[(-1, 0)])

    return brd[(-1, 0)], len([i for i in brd if brd[i] == 2]) #, [i for i in brd if brd[i] == 3], [i for i in brd if brd[i] == 4]

def solution():
    commands = read_number_from_file("day13", split=",")
    commands[0] = 2

    halt = True
    inp = 0

    while halt:
        commands, pnt, output1, output2, offset, halt = get_output(commands, inp)

    tiles = chunks(output1, 3)
    score, left = print_board(tiles)
    print("Score:", score)

from timeit import timeit
print(timeit(solution, number=1))