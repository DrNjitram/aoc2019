from boilerplates import read_number_from_file


def get_output(init_inst, v1, v2):
    init_inst[1] = v1
    init_inst[2] = v2

    inst_pnt = 0

    while init_inst[inst_pnt] != 99:
        instruction = init_inst[inst_pnt]
        if instruction == 1:
            init_inst[init_inst[inst_pnt + 3]] = init_inst[init_inst[inst_pnt + 1]] + init_inst[init_inst[inst_pnt + 2]]
        if instruction == 2:
            init_inst[init_inst[inst_pnt + 3]] = init_inst[init_inst[inst_pnt + 1]] * init_inst[init_inst[inst_pnt + 2]]
        inst_pnt += 4

    return init_inst[0]

desired = 19690720
instructions  = read_number_from_file(r"D:\AdventOfCode2019\probleminput\day2.txt", split=",")
prev = 0

print("Part 1:")
print(get_output(instructions[:], 12, 2))

print("Part 2:")

for i in range(0, 99):
    for j in range(0, 99):
        # with 0, 0 we get 29848
        a = i # adds 307200 to output
        b = j # add one to output
        try:
            output = get_output(instructions[:], a, b)
            if output == desired:
                print(a * 100 + b)
                exit()
        except IndexError:
            print("Values cause error")

