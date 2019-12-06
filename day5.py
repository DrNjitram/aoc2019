from boilerplates import read_number_from_file

def get_output(init_inst, system_id):
    inst_pnt = 0
    cnt = 0
    while init_inst[inst_pnt] != 99:
        cnt += 1
        instruction = init_inst[inst_pnt]

        positionals = str(instruction)[:-2][::-1] + "00"
        instruction = instruction % 100

        if positionals[0] == "1":
            pos_1 = init_inst[inst_pnt + 1]
        else:
            pos_1 = init_inst[init_inst[inst_pnt + 1]]

        if instruction not in [3, 4]:
            if positionals[1] == "1" :
                pos_2 = init_inst[inst_pnt + 2]
            else:
                pos_2 = init_inst[init_inst[inst_pnt + 2]]


        if instruction == 1:
            init_inst[init_inst[inst_pnt + 3]] = pos_1 + pos_2
            inst_pnt += 4
        elif instruction == 2:
            init_inst[init_inst[inst_pnt + 3]] = pos_1 * pos_2
            inst_pnt += 4
        if instruction == 3:
            init_inst[init_inst[inst_pnt + 1]] = system_id
            inst_pnt += 2
        elif instruction == 4:
            if pos_1 != 0:
                return pos_1
            #print("Output:", pos_1)
            inst_pnt += 2
        elif instruction == 5:
            inst_pnt = pos_2 if pos_1 != 0 else inst_pnt + 3
        elif instruction == 6:
            inst_pnt = pos_2 if pos_1 == 0 else inst_pnt + 3
        elif instruction == 7:
            init_inst[init_inst[inst_pnt + 3]] = 1 if pos_1 < pos_2 else 0
            inst_pnt += 4
        elif instruction == 8:
            init_inst[init_inst[inst_pnt + 3]] = 1 if pos_1 == pos_2 else 0
            inst_pnt += 4

    return init_inst[0]

program = read_number_from_file(r"D:\AdventOfCode2019\probleminput\day5.txt", split=",")

print("Part 1:", get_output(program[:], 1))
print("Part 2:", get_output(program[:], 5))

def solution():
    return get_output(program[:], 1) + get_output(program[:], 5)

from timeit import timeit
print(timeit(solution, number=1000)/1000)