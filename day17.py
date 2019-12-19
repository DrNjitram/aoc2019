from boilerplates import read_number_from_file
from intcode import get_output

def print_board(lst, printing = True):
    if printing:
        print("             111111111122222222223333333")
        print("   0123456789012345678901234567890123456")
        row = "00 "
        w = 0
        for i, ch in enumerate(lst):
            if ch != 10:
                row += chr(ch)
            else:
                if w == 0:
                    w = i

                print(row)
                row = str((i // w)).rjust(2, "0") + " "

    else:
        w = (len(lst) - 1)//lst.count(10)
    return w


def part1(cmd):
    output = get_output(cmd)
    plane = output[2]
    width = print_board(plane, True) + 1

    # Part 1
    score = 0
    for i in range(width + 1, len(plane) - 1 - width):
        ch = plane[i]
        if ch == 35:
            if plane[i - 1] == 35 and plane[i + 1] == 35 and plane[i - width] == 35 and plane[i + width]:
                score += (i % width) * (i // width)

    print(score)

def part2(cmd):
    main_routine = "A,A,B,C,A,C,B,C,A,B\n"
    A = "L,4,L,10,L,6\n"
    B = "L,6,L,4,R,8,R,8\n"
    C = "L,6,R,8,L,10,L,8,L,8\n"
    feed = "n\n"

    routine = [ord(c) for c in main_routine + A + B + C + feed]
    print(routine)
    cmd[0] = 2

    output = get_output(cmd, routine)
    print(output[2])
    print(output[3])
    print_board(output[2])



commands = read_number_from_file("day17", split=",")
#part1(commands[:])
part2(commands[:])


